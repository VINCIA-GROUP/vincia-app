import psycopg2
from adobe_api_functions import AdobeApiFunctions
from extract_csv_data import ExtractCsvData
from question_repository import QuestionRepository
from read_convert_file import ReadConvertFile
from alternative import Alternative
from extractor import Extractor
import os.path
import asyncio



async def extract_question(nome_prova, file_name_prova, file_name_data, dic_cod_prova, base_path, html_questions, count, total, question_repository):
    file_name_prova = file_name_prova.replace('.pdf', '')
    pdf_path_in = f"resources/{nome_prova}/{file_name_prova}.pdf"
    pdf_path_temp = f"temp/{nome_prova}/{file_name_prova}.zip"
    data_path = f"data/{file_name_data}"
    
  
    if os.path.isfile(pdf_path_temp) == False:
        await AdobeApiFunctions.extract_info_from_pdf(pdf_path_in, pdf_path_temp)

    pdf_path_temp_complete = f"{base_path}/{pdf_path_temp}"
    data = ReadConvertFile.read_zip_convert_in_object(pdf_path_temp_complete)

    try:
        if Extractor.is_a_question(data):
            extractor = Extractor()
            question = extractor.extract_question(data, pdf_path_temp_complete )

            ex = ExtractCsvData(dic_cod_prova, data_path)
            question_info = ex.get_info_question(question.info.num_question, question.info.area)
            
            question_repository.insert_question(nome_prova, question, question_info)
            connection.commit()
            
            html_questions.append(f"<br><div>{question.to_html()}</div>") 
    except Exception as e:
        print(f"falhou: {e}")
        pass
        
    print(f"{count}/{total}")
    
async def main_async():
    print("Inicio-Main1")
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/extract_questions_from_pdfs"
    html_questions = []
    
    
    # file_name_data = 'ITENS_PROVA_2020.csv'
    # nome_prova = 'Enem-2020'
    # dic_cod_prova = {
    #     'MT' : '695',
    #     'LC' : '691',
    #     'CN' : '699',
    #     'CH' : '687'
    # }
    # list_file_names = os.listdir(f"{base_path}/resources/{nome_prova}")
    
    list_file_names = os.listdir(f"{base_path}/resources/Enem-2021")
    file_name_data = 'ITENS_PROVA_2021.csv'
    nome_prova = 'Enem-2021'
    dic_cod_prova = {
        'MT': '1007',
        'LC':'1003',
        'CN':'1011',
        'CH':'999'
    }
    
    question_repository = QuestionRepository(connection)
    question_repository.insert_areas_and_abilities()

    # tasks = []
    count = 1
    for file_name in list_file_names:
        await extract_question(nome_prova, file_name, file_name_data, dic_cod_prova, base_path, html_questions, count, len(list_file_names), question_repository)
        # tasks.append(asyncio.create_task(extract_question(nome_prova, file_name, file_name_data, dic_cod_prova, base_path, html_questions, count, len(list_file_names), question_repository)))
        count += 1
    
    # await asyncio.gather(*tasks)
    
    connection.commit()

    with open("exemplo.html", "w", encoding="utf-8") as arquivo:
        for q in html_questions:
            arquivo.write(q)           
    print("Fim-Main1")
    
    
async def main2_async():
    print("Inicio-Main2") 
    file_name = "ENEM_2021_P1_CAD_07_DIA_2_AZUL-PG1"
    pdf_path_in = f"resources/{file_name}.pdf"
    pdf_path_temp = f"output/{file_name}.zip"
    await AdobeApiFunctions.extract_info_from_pdf(pdf_path_in, pdf_path_temp)
    print("Fim-Main2")


async def main3_async():
    print("Inicio-Main3") 
    path = f"data\ITENS_PROVA_2021.csv"
    ex = ExtractCsvData({'MT':'1007'},path)
    result = ex.get_info_question('136', 'matemática e suas tecnologias aaaa')
    print("Fim-Main3")


#Execução principal

from dotenv import load_dotenv

load_dotenv()

sc = os.environ["CONNECTION_STRING_DB"]    
connection = psycopg2.connect(sc, sslmode='require',)

asyncio.run(main_async())

connection.close()

