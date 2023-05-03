import json
import zipfile
import base64


class ReadConvertFile:
    def read_zip_convert_in_object(path):        
        with zipfile.ZipFile(path, 'r') as zip_ref:        
            # Lê o conteúdo de um arquivo específico
            with zip_ref.open('structuredData.json') as file:
                conteudo = file.read()
                return json.loads(conteudo)
    
    def read_img_convert_for_base64(path, pathImg):        
        with zipfile.ZipFile(path) as zip_ref:        
            with zip_ref.open(pathImg) as file:
                return base64.b64encode(file.read()).decode("utf-8")      
