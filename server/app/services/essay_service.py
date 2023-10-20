import openai
import json
from datetime import datetime
import os
from google.cloud import vision_v1
from dotenv import load_dotenv
import uuid
from google.oauth2 import service_account



load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Get the partial credentials JSON string from the environment variable
credentials_partial_str = os.getenv('GOOGLE_CREDENTIALS_PARTIAL')

# Parse the JSON string into a dictionary
credentials_dict = json.loads(credentials_partial_str)

# Add the other fields to the credentials dictionary
credentials_dict.update({
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/transcibeessay%40testsdl.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})

# Create a credentials object from the dictionary
credentials = service_account.Credentials.from_service_account_info(credentials_dict)

# Instantiate the Google Cloud Vision client
client = vision_v1.ImageAnnotatorClient(credentials=credentials)


class EssayService:
    def __init__(self, essay_repository, essay_additional_text_repository, essay_theme_repository):
        self.essay_repository = essay_repository
        self.essay_additional_text_repository = essay_additional_text_repository
        self.essay_theme_repository = essay_theme_repository
    
    def get_essay_history(self, user_id):
        """Retrieve a user's essay history."""
        response = self.essay_repository.get_by_user_id(user_id)
        self.essay_repository.commit()
        return response
    
    def get_unfinished_essays(self, user_id):
        """Retrieve a user's unfinished essays."""
        response = self.essay_repository.get_unfinished_by_user_id(user_id)
        self.essay_repository.commit()
        return response
    
    def create_new_essay(self, theme_id, user_id, title):
        result = self.essay_repository.insert_new_essay(str(uuid.uuid4()), theme_id, user_id, title, "", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "False")
        self.essay_repository.commit()
        return result
    
    def save_essay(self, essay):
        result = self.essay_repository.insert_essay(essay)
        self.essay_repository.commit()
        return result
    
    def delete_essay(self, essay_id):
        """Delete an essay by its ID."""
        response = self.essay_repository.delete_essay(essay_id)
        self.essay_repository.commit()
        return response

    def get_essay_analysis(self, essay_id, user_id, theme_id, essay_title, essay_content):
        # Construct the prompt
        prompt = (
            "Você é um corretor experiente do Enem. Um aluno está solicitando que você corrija a redação que ele está te mandando."
            "Usando os moldes de correção de redação do Enem, analise e dê nota (nota de 0 a 200 em cada competência) com base no tema proposto o título e a redação do seu aluno.\n"
            f"Tema: {essay_title}\n"
            "Título da redação: O titulo da redação é a primeira linha do texto da redação\n"
            f"Texto da redação: {essay_content}\n\n"
            "Por favor, retorne a analise da redação seguindo extritamente essa estrutura:\n"
            "C1 Nota: \n"
            "C2 Nota: \n"
            "C3 Nota: \n"
            "C4 Nota: \n"
            "C5 Nota: \n"
            "Nota Total: \n"
            "C1 Explicação: \n"
            "C2 Explicação: \n"
            "C3 Explicação: \n"
            "C4 Explicação: \n"
            "C5 Explicação: \n"
            "Explicação Geral: \n"
        )
        
        # Send a request to the ChatGPT API
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=3700,
            n=1,
            stop=None,
            temperature=0.7,
        )
        
        # Extract and parse the API response
        analysis_text = response.choices[0].text.strip()
        analysis_lines = analysis_text.split('\n')
        analysis_dict = {line.split(': ')[0]: line.split(': ')[1] for line in analysis_lines}
        
        # Construct the essay analysis entity
        essay_analysis = {
            "essay_id": essay_id,
            "user_id": user_id,
            "theme_id": theme_id,
            "title": essay_title,
            "content": essay_content,
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # current datetime in a string format
            "is_finished": True,  # assuming the analysis indicates a finished essay
            "c1_grade": analysis_dict["C1 Nota"],
            "c2_grade": analysis_dict["C2 Nota"],
            "c3_grade": analysis_dict["C3 Nota"],
            "c4_grade": analysis_dict["C4 Nota"],
            "c5_grade": analysis_dict["C5 Nota"],
            "total_grade": analysis_dict["Nota Total"],
            "c1_analysis": analysis_dict["C1 Explicação"],
            "c2_analysis": analysis_dict["C2 Explicação"],
            "c3_analysis": analysis_dict["C3 Explicação"],
            "c4_analysis": analysis_dict["C4 Explicação"],
            "c5_analysis": analysis_dict["C5 Explicação"],
            "general_analysis": analysis_dict["Explicação Geral"]
        }
        self.save_essay(essay_analysis)
        return essay_analysis

    def perform_ocr(content):
        image = vision_v1.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        if texts:
            return texts[0].description  # Return the entire text from the image
        return ""
