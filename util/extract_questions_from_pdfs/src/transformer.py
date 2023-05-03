from alternative import Alternative

class Transformer:
    def get_alternatives(elemets):
        alternatives = []
        i = 1
        while i < len(elemets):
            try:
                if len(elemets[i]['Text']) <= 2 and elemets[i]['Font']['weight'] == 700:
                    print(elemets[i]['Text'])
                    alternatives.append(Alternative( elemets[i]['Text'], elemets[i+1]['Text']))      
                    elemets.pop(i)
                    elemets.pop(i)
                    i -= 1
            except:
                pass
            i+= 1
        return alternatives
    

    def find_img_position(imgElement, nextElement):
        position = 0
        charBounds = nextElement['CharBounds']
        while position < len(charBounds): 
            img_top_position = imgElement['Bounds'][1] + (imgElement['Bounds'][3] - imgElement['Bounds'][1])/2
            img_left_position = imgElement['Bounds'][0]
            if charBounds[position][0] > img_left_position and charBounds[position][1] < img_top_position:
                return position
            position += 1
        