from adobe_api_functions import AdobeApiFunctions
from read_convert_file import ReadConvertFile
from alternative import Alternative
from extractor import Extractor
import os.path
import asyncio

async def extract_question(file_name, base_path, html_questions, count, total):
    file_name = file_name.replace('.pdf', '')
    pdf_path_in = f"resources/{file_name}.pdf"
    pdf_path_temp = f"temp/{file_name}.zip"


    await AdobeApiFunctions.extract_info_from_pdf(pdf_path_in, pdf_path_temp)
    
    pdf_path_temp_complete = f"{base_path}/{pdf_path_temp}"
    data = ReadConvertFile.read_zip_convert_in_object(pdf_path_temp_complete)

    try:
        if Extractor.is_a_question(data):
            extractor = Extractor()
            question = extractor.extract_question(data, pdf_path_temp_complete )
            html_questions.append(f"<br><div>{question.to_html()}</div>") 
    except:
        pass
        
    os.remove(pdf_path_temp_complete)
    print(f"{count}/{total}")
    
async def main_async():
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/extract_questions_from_pdfs"
    html_questions = []
    list_file_names = os.listdir(f"{base_path}/resources")

    tasks = []
    count = 1
    for file_name in list_file_names:
        tasks.append(asyncio.create_task(extract_question(file_name, base_path, html_questions, count, len(list_file_names))))
        count += 1
    
    await asyncio.gather(*tasks)

    with open("exemplo.html", "w", encoding="utf-8") as arquivo:
        for q in html_questions:
            arquivo.write(q)           
    print("Fim")
    
    
async def main2_async():
    print("Inicio") 
    file_name = "ENEM_2021_P1_CAD_07_DIA_2_AZUL-PG1"
    pdf_path_in = f"resources/{file_name}.pdf"
    pdf_path_temp = f"output/{file_name}.zip"
    await AdobeApiFunctions.extract_info_from_pdf(pdf_path_in, pdf_path_temp)
    print("Fim")


asyncio.run(main2_async())



