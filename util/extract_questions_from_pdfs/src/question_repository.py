from datetime import datetime
import os
import uuid
import psycopg2
from question import Question

class QuestionRepository:
    
    key_table_area = {
        'CN': {
            'id': '7e6c2d22-a6bb-472a-ac86-a1c29b1658e7',
            'name': 'Ciências da Natureza e suas Tecnologias'
            },
        'MT': {
            'id':'dbb6cee7-3cba-49ca-84eb-b1204d670f89',
            'name': 'Matemática e suas Tecnologias'
            },
        'LC':{
            'id':'76a3c2e5-8630-4607-af2d-68933a6dd13b',
            'name': 'Linguagens e Códigos'
            },
        'CH':{
            'id':'13cd1299-5ebb-4fef-8d57-93db495cb170',
            'name': 'Ciências Humanas e suas Tecnologias'
        }
    }

    key_table_ability={
        'LC' :{
            '1':'3cfe476d-a2f8-44c1-9d80-68f66f6a610a',
            '2':'fa296f2a-0134-49d7-b152-212394105a97',
            '3':'0a934c46-ed75-49d8-8e2a-22428407d76d',
            '4':'1709a1b8-6b74-4d47-ad0d-02f9e88715f2',
            '5':'90f77c1f-34dd-46e1-ac50-d879677f4071',
            '6':'a9e9c173-2007-4ec2-b368-9c0102f04cb3',
            '7':'602d9bd8-d59a-44a6-8db1-245d044b7df7',
            '8':'d48c509f-7bb4-441b-9a44-c25a287498e0',
            '9':'589f6afb-1386-4283-b8d9-6bbba5653c53'
        },
        'MT':{
            '1':'7ad5ed12-6722-421d-b29d-215cb7b444a6',
            '2':'17408fc2-235b-4238-aae2-1302cc6f9100',
            '3':'d57eb552-61a8-4a81-8879-c1534ec2d869',
            '4':'dbea4071-339a-42cb-a1a7-284f517ef495',
            '5':'c1ed8b3d-eb98-4da8-9a7d-409a82e8f6ae',
            '6':'196fbf5a-1756-41e2-9241-7a4529226132',
            '7':'8b748fc7-5ff1-4352-9cf4-eab1be46ac3c'
        },
        'CN':{
            '1':'b2f6c336-c875-4c62-aadc-ac78e9a086dd',
            '2':'4bb68e2b-ac1c-4b9a-8e91-4b587af3c6fb',
            '3':'10b38f18-9915-4e59-9a3d-e145bf3ffa4f',
            '4':'db0d3d18-d39b-40ab-ad4e-409622fe436a',
            '5':'2c6d72df-cbb9-404c-aa8f-029094bf2ee5',
            '6':'4e75548e-5dbf-47b5-a155-d20fe4f18221',
            '7':'39d34e3d-df73-4f98-97b7-01a9a7aa5f0d',
            '8':'e365be08-f415-4111-bfd6-ca7a50bac84c'
        },
        'CH':{
            '1':'9f06bff5-b6c0-42c0-a380-c4021158eeb0',
            '2':'ae8fe0c2-5b0a-4fc9-a0b6-123d458aad1e',
            '3':'6c68150a-d1e1-4cc5-abe7-d22083d37e00',
            '4':'fa4822e0-1086-4f03-95a3-9a50b35e017d',
            '5':'dc166f42-4585-479f-9eee-bed11a172b51',
            '6':'c52d211b-53d2-459d-a663-0f1ddacde441'
        }
    }
    
    hab_table = {
            'LC' : {
                '1': 'Aplicar as tecnologias da comunicação e da informação na escola, no trabalho e em outros contextos relevantes para sua vida.',
                '2': 'Conhecer e usar língua(s) estrangeira(s) moderna(s) como instrumento de acesso a informações e a outras culturas e grupos sociais.',
                '3': 'Compreender e usar a linguagem corporal como relevante para a própria vida, integradora social e formadora da identidade.',
                '4': 'Compreender a arte como saber cultural e estético gerador de significação e integrador da organização do mundo e da própria identidade.',
                '5': 'Analisar, interpretar e aplicar recursos expressivos das linguagens, relacionando textos com seus contextos, mediante a natureza, função, organização, estrutura das manifestações, de acordo com as condições de produção e recepção.',
                '6': 'Compreender e usar os sistemas simbólicos das diferentes linguagens como meios de organização cognitiva da realidade pela constituição de significados, expressão, comunicação e informação.',
                '7': 'Confrontar opiniões e pontos de vista sobre as diferentes linguagens e suas manifestações específicas.',
                '8': '- Compreender e usar a língua portuguesa como língua materna, geradora de significação e integradora da organização do mundo e da própria identidade.',
                '9': 'Entender os princípios, a natureza, a função e o impacto das tecnologias da comunicação e da informação na sua vida pessoal e social, no desenvolvimento do conhecimento, associando-o aos conhecimentos científicos, às linguagens que lhes dão suporte, às demais tecnologias, aos processos de produção e aos problemas que se propõem solucionar.'
            },
            'MT' : {
                '1': 'Construir significados para os números naturais, inteiros, racionais e reais.',
                '2': 'Utilizar o conhecimento geométrico para realizar a leitura e a representação da realidade e agir sobre ela.',
                '3': 'Construir noções de grandezas e medidas para a compreensão da realidade e a solução de problemas do cotidiano.',
                '4': 'Construir noções de variação de grandezas para a compreensão da realidade e a solução de problemas do cotidiano.',
                '5': 'Modelar e resolver problemas que envolvem variáveis socioeconômicas ou técnico-científicas, usando representações algébricas.',
                '6': 'Interpretar informações de natureza científica e social obtidas da leitura de gráficos e tabelas, realizando previsão de tendência, extrapolação, interpolação e interpretação.',
                '7': 'Compreender o caráter aleatório e não-determinístico dos fenômenos naturais e sociais e utilizar instrumentos adequados para medidas, determinação de amostras e cálculos de probabilidade para interpretar informações de variáveis apresentadas em uma distribuição estatística.',
            },
            'CN' : {
                '1': 'Compreender as ciências naturais e as tecnologias a elas associadas como construções humanas, percebendo seus papéis nos processos de produção e no desenvolvimento econômico e social da humanidade.',
                '2':'Identificar a presença e aplicar as tecnologias associadas às ciências naturais em diferentes contextos.',
                '3': 'Associar intervenções que resultam em degradação ou conservação ambiental a processos produtivos e sociais e a instrumentos ou ações científico-tecnológicos.',
                '4': 'Compreender interações entre organismos e ambiente, em particular aquelas relacionadas à saúde humana, relacionando conhecimentos científicos, aspectos culturais e características individuais.',
                '5': 'Entender métodos e procedimentos próprios das ciências naturais e aplicá-los em diferentes contextos.',
                '6': 'Apropriar-se de conhecimentos da física para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.',
                '7': 'Apropriar-se de conhecimentos da química para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.',
                '8': 'Apropriar-se de conhecimentos da biologia para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'
            },
            'CH' : {
                '1': 'Compreender os elementos culturais que constituem as identidades.',
                '2': 'Compreender as transformações dos espaços geográficos como produto das relações socioeconômicas e culturais de poder.',
                '3': 'Compreender a produção e o papel histórico das instituições sociais, políticas e econômicas, associando-as aos diferentes grupos conflitos e movimentos sociais.',
                '4': 'Entender as transformações técnicas e tecnológicas e seu impacto nos processos de produção, no desenvolvimento do conhecimento e na vida social.',
                '5': 'Utilizar os conhecimentos históricos para compreender e valorizar os fundamentos da cidadania e da democracia, favorecendo uma atuação consciente do indivíduo na sociedade.',
                '6': 'Compreender a sociedade e a natureza, reconhecendo suas interações no espaço em diferentes contextos históricos e geográficos'
            }
        }
    
    def __init__(self, connection):
        self.connection= connection
    
    def insert_question(self, title_statment, question:Question, question_info):
        cursor = self.connection.cursor()

        question_id = str(uuid.uuid4())
        answer_id = str(uuid.uuid4())
        ability_id = self.key_table_ability[question_info['area']][question_info['ability']]
        statement = f'<p>[{title_statment}-N{str(question.info.num_question)}]</p>' + str(question.statement)

        cursor.execute(f"INSERT INTO questions (id, statement, answer, rating, rating_deviation, volatility, last_rating_update, is_essay, ability_id) VALUES ('{question_id}', %s , '{answer_id}', '{int(question_info['rating'])}', 50, 0.2, %s, false, '{ability_id}');", (statement, datetime.utcnow().date()))

        for alternative in question.alternatives:
            alt_id = str(uuid.uuid4())
            if(alternative.letter == question_info['answer']):
                alt_id = answer_id
            cursor.execute(f"INSERT INTO alternatives (id, text, question_id) VALUES ('{alt_id}', %s, '{question_id}');", (alternative.text, ))
        cursor.close()
    
    
    def insert_areas_and_abilities(self):
        self.insert_areas()
        self.insert_abilities()
        self.connection.commit()
        
    def insert_areas(self):
        cursor = self.connection.cursor()
        keys = list(self.key_table_area.keys())
        for key in keys:
            try:
                cursor.execute(f"INSERT INTO areas (id, name, description) VALUES ('{self.key_table_area[key]['id']}', '{self.key_table_area[key]['name']}', 'Description {self.key_table_area[key]['name']}' );")
            except:
                continue
        cursor.close()
        
    def insert_abilities(self):
        cursor = self.connection.cursor()
        keys = list(self.key_table_ability.keys())
        for key in keys:
            keys_abilities = list(self.key_table_ability[key].keys())
            for key_ability in keys_abilities:
                try:
                    cursor.execute(f"INSERT INTO abilities (id, name, description, area_id) VALUES ('{self.key_table_ability[key][key_ability]}', '{self.hab_table[key][key_ability]}', 'Description {self.hab_table[key][key_ability]}', '{self.key_table_area[key]['id']}');")
                except:
                    continue
        cursor.close()