from alternative import Alternative
from info_question import InfoQuestion
from read_convert_file import ReadConvertFile
from question import Question

class Extractor:
    
    def is_a_question(data):
        textFirstElement = data['elements'][0]['Text'].lower()
        textSecondElement = data['elements'][1]['Text'].lower()
        return 'questão' in textFirstElement or 'questão' in textSecondElement
    
    def extract_question(self, data, path):
        info_question = self.extract_info_question(data)
        alternatives = self.extract_alternatives(data, path)
        statement = self.extract_statement(data, path)
        return Question(info_question, statement, alternatives)
    
    def extract_info_question(self, data):
        if 'questão' in data['elements'][0]['Text'].lower():        
            textFirstElement = data['elements'][0]['Text'].lower()
            data['elements'].pop(0)
        else:
            textFirstElement = data['elements'][1]['Text'].lower()
            data['elements'].pop(0)
            data['elements'].pop(0)
        text_first_element_split = textFirstElement.split('-')
        num_question = text_first_element_split[0].split(' ')[1]
        area = text_first_element_split[1]
        return InfoQuestion(num_question, area)
    
    def extract_statement(self, data, path):
        elements = data['elements']
        index = 0
        statement = "<p>"
        while index < len(elements):
            title = self._extract_title_if_its(elements[index])
            if len(title) > 0:
                statement += title
                index += 1
                continue 
                
            citation = self._extract_citation_if_its(elements[index])
            if len(citation) > 0:
                statement += citation
                index += 1
                continue              
                
            image =  self._extract_image_if_its(elements, index, path)
            if len(image) > 0:
                statement += image
                index += 1
                continue 

            try:
                statement += elements[index]['Text'] 
                if len(elements[index]['Text']) <= 70:
                    statement += '<br>'
            except:
                imagen_in_text = self._extract_image_if_its_in_the_text(elements, index,  path)
                if len(imagen_in_text) > 0:
                    statement += imagen_in_text
                    index += 2
                    continue 
            index += 1
        statement += '</p>'
        return statement
    
    def extract_alternatives(self, data, path):
        alternatives = []
        alternatives_elements = self._get_alternatives_elements(data)
        for alternatives_element in alternatives_elements:
            paragraph = self._convert_element_list_in_paragraph_html(alternatives_element['elements'], path)
            alternatives.append(Alternative(alternatives_element['letter'], paragraph))
        return alternatives
    
    def _extract_title_if_its(self, element):
        return ''
    
    def _extract_citation_if_its(self, element):
        try:
            if(element['attributes']['TextAlign'] == "End"):
                text = element['Text']
                return f'</p><p id="citation" style="text-align: right;">{text}</p><p>'
        except:
            pass
        return ""
        
    def _extract_image_if_its(self, elements, index, path):
        try:
            img_element = elements[index]
            img_path = img_element['filePaths'][0]
            encoding = ReadConvertFile.read_img_convert_for_base64(path, img_path)
            try:
                if self._image_is_in_the_text(img_element, elements[index +1]) == False:
                    return  f'</p><img src="data:image/png;base64,{encoding}"><p>'  
            except:
                return f'</p><img src="data:image/png;base64,{encoding}"><p>' 
        except:
            pass
        return ""
    
    def _extract_image_if_its_in_the_text(self, elements, index, path):
        try:
            img_element = elements[index]
            next_element = elements[index +1]
            if self._image_is_in_the_text(img_element, next_element):
                return self._convert_img_in_html_base64(img_element, next_element, path)
        except:
            pass
        return ""
    
    def _image_is_in_the_text(self, img_element, next_element):
        return next_element['CharBounds'][0][1] > img_element['Bounds'][1]
    
    
    
    def _convert_element_list_in_paragraph_html(self, elements, path):
        paragraph = "<p>"
        index = 0
        while index < len(elements):
            try:
                paragraph += elements[index]['Text']
            except:
                try:
                    img_element = elements[index]
                    next_element = elements[index+1]
                    paragraph += self._convert_img_in_html_base64(img_element, next_element, path)
                    index +=1
                except:
                    pass
            index += 1
        paragraph += "</p>"
        return paragraph
    
    def _convert_img_in_html_base64(self, img_element, next_element, path):
        img_path = img_element['filePaths'][0]
        encoding = ReadConvertFile.read_img_convert_for_base64(path, img_path)
        image_position = self._find_img_position(img_element, next_element)
        text_next_element = next_element['Text']
        new_text = f'{text_next_element[:image_position]}<img src="data:image/png;base64,{encoding}">{text_next_element[image_position:]}'   
        return new_text
    
    def _get_alternatives_elements(self, data):
        elements = data['elements']
        alternatives_elements= []
        alternatives_elements_info= []
        letters_alternatives_elements = ['A', 'B', 'C', 'D', 'E']
        i_alternatives_elements = 0
        i = 1
        while i < len(elements):
            try:         
                if len(elements[i]['Text']) <= 4 and elements[i]['Font']['weight'] == 700 and letters_alternatives_elements[i_alternatives_elements] in elements[i]['Text'].upper().strip():                    
                    
                    alternatives_elements_info.append({"letter":  letters_alternatives_elements[i_alternatives_elements], "init": i, "final": i+1})                    
                    
                    if (i_alternatives_elements > 0):
                        alternatives_elements_info[i_alternatives_elements -1]['final'] = i - 1
                        
                    if (i_alternatives_elements >= len(letters_alternatives_elements)-1):
                        alternatives_elements_info[i_alternatives_elements]['final'] = len(elements)-1 
                        
                    i_alternatives_elements += 1 
            except:
                pass
            i+= 1
        
        if(len(alternatives_elements_info) == len(letters_alternatives_elements)):
            for info in alternatives_elements_info:
                elementsList = []
                indexElement = info['init'] + 1
                while indexElement <= info['final']:
                    elementsList.append(elements[indexElement])
                    indexElement += 1
                indexElement = info['init'] + 1
                alternatives_elements.append({'letter': info['letter'], 'elements': elementsList})
            i = alternatives_elements_info[len(letters_alternatives_elements)-1]['final']
            while i >= alternatives_elements_info[0]['init']:
                data['elements'].pop(i)
                i -= 1
            return alternatives_elements
                    
    
    

    def _find_img_position(self, imgElement, nextElement):
        position = 0
        charBounds = nextElement['CharBounds']
        while position < len(charBounds): 
            img_top_position = imgElement['Bounds'][1] + (imgElement['Bounds'][3] - imgElement['Bounds'][1])/2
            img_left_position = imgElement['Bounds'][0]
            if charBounds[position][0] > img_left_position and charBounds[position][1] < img_top_position:
                return position
            position += 1
        