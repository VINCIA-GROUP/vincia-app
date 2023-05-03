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
    textFirstElementSplit = textFirstElement.split('-')
    numQuestao = textFirstElementSplit[0].split(' ')[1]
    area = textFirstElementSplit[1]
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
                imgElement = elemets[i]
                imgPath = imgElement['filePaths'][0]
                encoding = ReadConvertFile.read_img_convert_for_base64(f"{base_path}/{pdf_path_out}", imgPath)
                nextElement = elemets[i+1]
                try:
                    if nextElement['CharBounds'][0][1] > imgElement['Bounds'][1]:
                        imagePosition = Transformer.find_img_position(imgElement, nextElement)
                        textNextElement = nextElement['Text']
                        newText = f'{textNextElement[:imagePosition]}<img src="data:image/png;base64,{encoding}">{textNextElement[imagePosition:]}'   
                        elemets[i+1]['Text'] = newText
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


