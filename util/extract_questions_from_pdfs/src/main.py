from adobe_api_functions import AdobeApiFunctions
from read_convert_file import ReadConvertFile
from alternative import Alternative
from transformer import Transformer
import os.path


#1 - Ler aquirvo pdf

#2 - Dividir arquivo em páginas
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/extract_questions_from_pdfs"
pdf_path_in = "resources/EX94-DIA2.pdf"
pdf_path_out = "output/EX94-DIA2-v1.zip"


#AdobeApiFunctions.extract_info_from_pdf(pdf_path_in, pdf_path_out)

data = ReadConvertFile.read_zip_convert_in_object(f"{base_path}/{pdf_path_out}")

textFirstElement = data['elements'][0]['Text'].lower()

if 'questão' in textFirstElement:
    text_first_element_split = textFirstElement.split('-')
    num_questao = text_first_element_split[0].split(' ')[1]
    area = text_first_element_split[1]
    alternativas = []
    enuciado = ""
    aa = False
    
    elemets = data['elements'] 
    
    alternativas = Transformer.get_alternatives(elemets)
        
    i = 1
    while i < len(elemets):
        try:
            enuciado += f"<p>{elemets[i]['Text']}"
        except:
            try:
                img_element = elemets[i]
                img_path = img_element['filePaths'][0]
                encoding = ReadConvertFile.read_img_convert_for_base64(f"{base_path}/{pdf_path_out}", img_path)
                next_element = elemets[i+1]
                try:
                    if next_element['CharBounds'][0][1] > img_element['Bounds'][1]:
                        image_position = Transformer.find_img_position(img_element, next_element)
                        text_next_element = next_element['Text']
                        new_text = f'{text_next_element[:image_position]}<img src="data:image/png;base64,{encoding}">{text_next_element[image_position:]}'   
                        elemets[i+1]['Text'] = new_text
                    else:
                        enuciado += f'</p><img src="data:image/png;base64,{encoding}"><p>'    
                except:
                    enuciado += f'</p><img src="data:image/png;base64,{encoding}"><p>'
                    pass
            except:
                pass
            pass
        i += 1
        
    with open("exemplo.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(enuciado)
    

  
            
        
print("fim")


