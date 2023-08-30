import csv
import difflib

class ExtractCsvData:
    hab_table = {
            'LC' : {
                '1' : {'cod': '1', 'name': 'Aplicar as tecnologias da comunicação e da informação na escola, no trabalho e em outros contextos relevantes para sua vida.'},
                '2' : {'cod': '1', 'name': 'Aplicar as tecnologias da comunicação e da informação na escola, no trabalho e em outros contextos relevantes para sua vida.'},
                '3' : {'cod': '1', 'name': 'Aplicar as tecnologias da comunicação e da informação na escola, no trabalho e em outros contextos relevantes para sua vida.'},
                '4' : {'cod': '1', 'name': 'Aplicar as tecnologias da comunicação e da informação na escola, no trabalho e em outros contextos relevantes para sua vida.'},
                '5' : {'cod': '2', 'name': 'Conhecer e usar língua(s) estrangeira(s) moderna(s) como instrumento de acesso a informações e a outras culturas e grupos sociais.'},
                '6' : {'cod': '2', 'name': 'Conhecer e usar língua(s) estrangeira(s) moderna(s) como instrumento de acesso a informações e a outras culturas e grupos sociais.'},
                '7' : {'cod': '2', 'name': 'Conhecer e usar língua(s) estrangeira(s) moderna(s) como instrumento de acesso a informações e a outras culturas e grupos sociais.'},
                '8' : {'cod': '2', 'name': 'Conhecer e usar língua(s) estrangeira(s) moderna(s) como instrumento de acesso a informações e a outras culturas e grupos sociais.'},
                '9' : {'cod': '3', 'name': 'Compreender e usar a linguagem corporal como relevante para a própria vida, integradora social e formadora da identidade.'},
                '10' : {'cod': '3', 'name': 'Compreender e usar a linguagem corporal como relevante para a própria vida, integradora social e formadora da identidade.'},
                '11' : {'cod': '3', 'name': 'Compreender e usar a linguagem corporal como relevante para a própria vida, integradora social e formadora da identidade.'},
                '12' : {'cod': '4', 'name': 'Compreender a arte como saber cultural e estético gerador de significação e integrador da organização do mundo e da própria identidade.'},
                '13' : {'cod': '4', 'name': 'Compreender a arte como saber cultural e estético gerador de significação e integrador da organização do mundo e da própria identidade.'},
                '14' : {'cod': '4', 'name': 'Compreender a arte como saber cultural e estético gerador de significação e integrador da organização do mundo e da própria identidade.'},
                '15' : {'cod': '5', 'name': 'Analisar, interpretar e aplicar recursos expressivos das linguagens, relacionando textos com seus contextos, mediante a natureza, função, organização, estrutura das manifestações, de acordo com as condições de produção e recepção.'},
                '16' : {'cod': '5', 'name': 'Analisar, interpretar e aplicar recursos expressivos das linguagens, relacionando textos com seus contextos, mediante a natureza, função, organização, estrutura das manifestações, de acordo com as condições de produção e recepção.'},
                '17' : {'cod': '5', 'name': 'Analisar, interpretar e aplicar recursos expressivos das linguagens, relacionando textos com seus contextos, mediante a natureza, função, organização, estrutura das manifestações, de acordo com as condições de produção e recepção.'},
                '18' : {'cod': '6', 'name': 'Compreender e usar os sistemas simbólicos das diferentes linguagens como meios de organização cognitiva da realidade pela constituição de significados, expressão, comunicação e informação.'},
                '19' : {'cod': '6', 'name': 'Compreender e usar os sistemas simbólicos das diferentes linguagens como meios de organização cognitiva da realidade pela constituição de significados, expressão, comunicação e informação.'},
                '20' : {'cod': '6', 'name': 'Compreender e usar os sistemas simbólicos das diferentes linguagens como meios de organização cognitiva da realidade pela constituição de significados, expressão, comunicação e informação.'},
                '21' : {'cod': '7', 'name': 'Confrontar opiniões e pontos de vista sobre as diferentes linguagens e suas manifestações específicas.'},
                '22' : {'cod': '7', 'name': 'Confrontar opiniões e pontos de vista sobre as diferentes linguagens e suas manifestações específicas.'},
                '23' : {'cod': '7', 'name': 'Confrontar opiniões e pontos de vista sobre as diferentes linguagens e suas manifestações específicas.'},
                '24' : {'cod': '7', 'name': 'Confrontar opiniões e pontos de vista sobre as diferentes linguagens e suas manifestações específicas.'},
                '25' : {'cod': '8', 'name': '- Compreender e usar a língua portuguesa como língua materna, geradora de significação e integradora da organização do mundo e da própria identidade.'},
                '26' : {'cod': '8', 'name': 'Compreender e usar a língua portuguesa como língua materna, geradora de significação e integradora da organização do mundo e da própria identidade.'},
                '27' : {'cod': '8', 'name': 'Compreender e usar a língua portuguesa como língua materna, geradora de significação e integradora da organização do mundo e da própria identidade.'},
                '28' : {'cod': '9', 'name': 'Entender os princípios, a natureza, a função e o impacto das tecnologias da comunicação e da informação na sua vida pessoal e social, no desenvolvimento do conhecimento, associando-o aos conhecimentos científicos, às linguagens que lhes dão suporte, às demais tecnologias, aos processos de produção e aos problemas que se propõem solucionar.'},
                '29' : {'cod': '9', 'name': 'Entender os princípios, a natureza, a função e o impacto das tecnologias da comunicação e da informação na sua vida pessoal e social, no desenvolvimento do conhecimento, associando-o aos conhecimentos científicos, às linguagens que lhes dão suporte, às demais tecnologias, aos processos de produção e aos problemas que se propõem solucionar.'},
                '30' : {'cod': '9', 'name': 'Entender os princípios, a natureza, a função e o impacto das tecnologias da comunicação e da informação na sua vida pessoal e social, no desenvolvimento do conhecimento, associando-o aos conhecimentos científicos, às linguagens que lhes dão suporte, às demais tecnologias, aos processos de produção e aos problemas que se propõem solucionar.'},
            },
            'MT' : {
                '1' : {'cod': '1', 'name': 'Construir significados para os números naturais, inteiros, racionais e reais.'},
                '2' : {'cod': '1', 'name': 'Construir significados para os números naturais, inteiros, racionais e reais.'},
                '3' : {'cod': '1', 'name': 'Construir significados para os números naturais, inteiros, racionais e reais.'},
                '4' : {'cod': '1', 'name': 'Construir significados para os números naturais, inteiros, racionais e reais.'},
                '5' : {'cod': '1', 'name': 'Construir significados para os números naturais, inteiros, racionais e reais.'},
                '6' : {'cod': '2', 'name': 'Utilizar o conhecimento geométrico para realizar a leitura e a representação da realidade e agir sobre ela.'},
                '7' : {'cod': '2', 'name': 'Utilizar o conhecimento geométrico para realizar a leitura e a representação da realidade e agir sobre ela.'},
                '8' : {'cod': '2', 'name': 'Utilizar o conhecimento geométrico para realizar a leitura e a representação da realidade e agir sobre ela.'},
                '9' : {'cod': '2', 'name': 'Utilizar o conhecimento geométrico para realizar a leitura e a representação da realidade e agir sobre ela.'},
                '10' : {'cod': '3', 'name': 'Construir noções de grandezas e medidas para a compreensão da realidade e a solução de problemas do cotidiano.'},
                '11' : {'cod': '3', 'name': 'Construir noções de grandezas e medidas para a compreensão da realidade e a solução de problemas do cotidiano.'},
                '12' : {'cod': '3', 'name': 'Construir noções de grandezas e medidas para a compreensão da realidade e a solução de problemas do cotidiano.'},
                '13' : {'cod': '3', 'name': 'Construir noções de grandezas e medidas para a compreensão da realidade e a solução de problemas do cotidiano.'},
                '14' : {'cod': '3', 'name': 'Construir noções de grandezas e medidas para a compreensão da realidade e a solução de problemas do cotidiano.'},
                '15' : {'cod': '4', 'name': 'Construir noções de variação de grandezas para a compreensão da realidade e a solução de problemas do cotidiano.'},
                '16' : {'cod': '4', 'name': 'Construir noções de variação de grandezas para a compreensão da realidade e a solução de problemas do cotidiano.'},
                '17' : {'cod': '4', 'name': 'Construir noções de variação de grandezas para a compreensão da realidade e a solução de problemas do cotidiano.'},
                '18' : {'cod': '4', 'name': 'Construir noções de variação de grandezas para a compreensão da realidade e a solução de problemas do cotidiano.'},
                '19' : {'cod': '5', 'name': 'Modelar e resolver problemas que envolvem variáveis socioeconômicas ou técnico-científicas, usando representações algébricas.'},
                '20' : {'cod': '5', 'name': 'Modelar e resolver problemas que envolvem variáveis socioeconômicas ou técnico-científicas, usando representações algébricas.'},
                '21' : {'cod': '5', 'name': 'Modelar e resolver problemas que envolvem variáveis socioeconômicas ou técnico-científicas, usando representações algébricas.'},
                '22' : {'cod': '5', 'name': 'Modelar e resolver problemas que envolvem variáveis socioeconômicas ou técnico-científicas, usando representações algébricas.'},
                '23' : {'cod': '5', 'name': 'Modelar e resolver problemas que envolvem variáveis socioeconômicas ou técnico-científicas, usando representações algébricas.'},
                '24' : {'cod': '6', 'name': 'Interpretar informações de natureza científica e social obtidas da leitura de gráficos e tabelas, realizando previsão de tendência, extrapolação, interpolação e interpretação.'},
                '25' : {'cod': '6', 'name': 'Interpretar informações de natureza científica e social obtidas da leitura de gráficos e tabelas, realizando previsão de tendência, extrapolação, interpolação e interpretação.'},
                '26' : {'cod': '6', 'name': 'Interpretar informações de natureza científica e social obtidas da leitura de gráficos e tabelas, realizando previsão de tendência, extrapolação, interpolação e interpretação.'},
                '27' : {'cod': '7', 'name': 'Compreender o caráter aleatório e não-determinístico dos fenômenos naturais e sociais e utilizar instrumentos adequados para medidas, determinação de amostras e cálculos de probabilidade para interpretar informações de variáveis apresentadas em uma distribuição estatística.'},
                '28' : {'cod': '7', 'name': 'Compreender o caráter aleatório e não-determinístico dos fenômenos naturais e sociais e utilizar instrumentos adequados para medidas, determinação de amostras e cálculos de probabilidade para interpretar informações de variáveis apresentadas em uma distribuição estatística.'},
                '29' : {'cod': '7', 'name': 'Compreender o caráter aleatório e não-determinístico dos fenômenos naturais e sociais e utilizar instrumentos adequados para medidas, determinação de amostras e cálculos de probabilidade para interpretar informações de variáveis apresentadas em uma distribuição estatística.'},
                '30' : {'cod': '7', 'name': 'Compreender o caráter aleatório e não-determinístico dos fenômenos naturais e sociais e utilizar instrumentos adequados para medidas, determinação de amostras e cálculos de probabilidade para interpretar informações de variáveis apresentadas em uma distribuição estatística.'},
            },
            'CN' : {
                '1' : {'cod': '1', 'name': 'Compreender as ciências naturais e as tecnologias a elas associadas como construções humanas, percebendo seus papéis nos processos de produção e no desenvolvimento econômico e social da humanidade.'},
                '2' : {'cod': '1', 'name': 'Compreender as ciências naturais e as tecnologias a elas associadas como construções humanas, percebendo seus papéis nos processos de produção e no desenvolvimento econômico e social da humanidade.'},
                '3' : {'cod': '1', 'name': 'Compreender as ciências naturais e as tecnologias a elas associadas como construções humanas, percebendo seus papéis nos processos de produção e no desenvolvimento econômico e social da humanidade.'},
                '4' : {'cod': '1', 'name': 'Compreender as ciências naturais e as tecnologias a elas associadas como construções humanas, percebendo seus papéis nos processos de produção e no desenvolvimento econômico e social da humanidade.'},
                '5' : {'cod': '2', 'name': 'Identificar a presença e aplicar as tecnologias associadas às ciências naturais em diferentes contextos.'},
                '6' : {'cod': '2', 'name': 'Identificar a presença e aplicar as tecnologias associadas às ciências naturais em diferentes contextos.'},
                '7' : {'cod': '2', 'name': 'Identificar a presença e aplicar as tecnologias associadas às ciências naturais em diferentes contextos.'},
                '8' : {'cod': '3', 'name': 'Associar intervenções que resultam em degradação ou conservação ambiental a processos produtivos e sociais e a instrumentos ou ações científico-tecnológicos.'},
                '9' : {'cod': '3', 'name': 'Associar intervenções que resultam em degradação ou conservação ambiental a processos produtivos e sociais e a instrumentos ou ações científico-tecnológicos.'},
                '10' : {'cod': '3', 'name': 'Associar intervenções que resultam em degradação ou conservação ambiental a processos produtivos e sociais e a instrumentos ou ações científico-tecnológicos.'},
                '11' : {'cod': '3', 'name': 'Associar intervenções que resultam em degradação ou conservação ambiental a processos produtivos e sociais e a instrumentos ou ações científico-tecnológicos.'},
                '12' : {'cod': '3', 'name': 'Associar intervenções que resultam em degradação ou conservação ambiental a processos produtivos e sociais e a instrumentos ou ações científico-tecnológicos.'},
                '13' : {'cod': '4', 'name': 'Compreender interações entre organismos e ambiente, em particular aquelas relacionadas à saúde humana, relacionando conhecimentos científicos, aspectos culturais e características individuais.'},
                '14' : {'cod': '4', 'name': 'Compreender interações entre organismos e ambiente, em particular aquelas relacionadas à saúde humana, relacionando conhecimentos científicos, aspectos culturais e características individuais.'},
                '15' : {'cod': '4', 'name': 'Compreender interações entre organismos e ambiente, em particular aquelas relacionadas à saúde humana, relacionando conhecimentos científicos, aspectos culturais e características individuais.'},
                '16' : {'cod': '4', 'name': 'Compreender interações entre organismos e ambiente, em particular aquelas relacionadas à saúde humana, relacionando conhecimentos científicos, aspectos culturais e características individuais.'},
                '17' : {'cod': '5', 'name': 'Entender métodos e procedimentos próprios das ciências naturais e aplicá-los em diferentes contextos.'},
                '18' : {'cod': '5', 'name': 'Entender métodos e procedimentos próprios das ciências naturais e aplicá-los em diferentes contextos.'},
                '19' : {'cod': '5', 'name': 'Entender métodos e procedimentos próprios das ciências naturais e aplicá-los em diferentes contextos.'},
                '20' : {'cod': '6', 'name': 'Apropriar-se de conhecimentos da física para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
                '21' : {'cod': '6', 'name': 'Apropriar-se de conhecimentos da física para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
                '22' : {'cod': '6', 'name': 'Apropriar-se de conhecimentos da física para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
                '23' : {'cod': '6', 'name': 'Apropriar-se de conhecimentos da física para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
                '24' : {'cod': '7', 'name': 'Apropriar-se de conhecimentos da química para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
                '25' : {'cod': '7', 'name': 'Apropriar-se de conhecimentos da química para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
                '26' : {'cod': '7', 'name': 'Apropriar-se de conhecimentos da química para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
                '27' : {'cod': '7', 'name': 'Apropriar-se de conhecimentos da química para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
                '28' : {'cod': '8', 'name': 'Apropriar-se de conhecimentos da biologia para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
                '29' : {'cod': '8', 'name': 'Apropriar-se de conhecimentos da biologia para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
                '30' : {'cod': '8', 'name': 'Apropriar-se de conhecimentos da biologia para, em situações problema, interpretar, avaliar ou planejar intervenções científicotecnológicas.'},
            },
            'CH' : {
                '1' : {'cod': '1', 'name': 'Compreender os elementos culturais que constituem as identidades.'},
                '2' : {'cod': '1', 'name': 'Compreender os elementos culturais que constituem as identidades.'},
                '3' : {'cod': '1', 'name': 'Compreender os elementos culturais que constituem as identidades.'},
                '4' : {'cod': '1', 'name': 'Compreender os elementos culturais que constituem as identidades.'},
                '5' : {'cod': '1', 'name': 'Compreender os elementos culturais que constituem as identidades.'}, 
                '6' : {'cod': '2', 'name': 'Compreender as transformações dos espaços geográficos como produto das relações socioeconômicas e culturais de poder.'}, 
                '7' : {'cod': '2', 'name': 'Compreender as transformações dos espaços geográficos como produto das relações socioeconômicas e culturais de poder.'}, 
                '8' : {'cod': '2', 'name': 'Compreender as transformações dos espaços geográficos como produto das relações socioeconômicas e culturais de poder.'}, 
                '9' : {'cod': '2', 'name': 'Compreender as transformações dos espaços geográficos como produto das relações socioeconômicas e culturais de poder.'}, 
                '10' : {'cod': '2', 'name': 'Compreender as transformações dos espaços geográficos como produto das relações socioeconômicas e culturais de poder.'},
                '11' : {'cod': '3', 'name': 'Compreender a produção e o papel histórico das instituições sociais, políticas e econômicas, associando-as aos diferentes grupos, conflitos e movimentos sociais.'},
                '12' : {'cod': '3', 'name': 'Compreender a produção e o papel histórico das instituições sociais, políticas e econômicas, associando-as aos diferentes grupos, conflitos e movimentos sociais.'},
                '13' : {'cod': '3', 'name': 'Compreender a produção e o papel histórico das instituições sociais, políticas e econômicas, associando-as aos diferentes grupos, conflitos e movimentos sociais.'},
                '14' : {'cod': '3', 'name': 'Compreender a produção e o papel histórico das instituições sociais, políticas e econômicas, associando-as aos diferentes grupos, conflitos e movimentos sociais.'},
                '15' : {'cod': '3', 'name': 'Compreender a produção e o papel histórico das instituições sociais, políticas e econômicas, associando-as aos diferentes grupos, conflitos e movimentos sociais.'},
                '16' : {'cod': '4', 'name': 'Entender as transformações técnicas e tecnológicas e seu impacto nos processos de produção, no desenvolvimento do conhecimento e na vida social.'},
                '17' : {'cod': '4', 'name': 'Entender as transformações técnicas e tecnológicas e seu impacto nos processos de produção, no desenvolvimento do conhecimento e na vida social.'},
                '18' : {'cod': '4', 'name': 'Entender as transformações técnicas e tecnológicas e seu impacto nos processos de produção, no desenvolvimento do conhecimento e na vida social.'},
                '19' : {'cod': '4', 'name': 'Entender as transformações técnicas e tecnológicas e seu impacto nos processos de produção, no desenvolvimento do conhecimento e na vida social.'},
                '20' : {'cod': '4', 'name': 'Entender as transformações técnicas e tecnológicas e seu impacto nos processos de produção, no desenvolvimento do conhecimento e na vida social.'},
                '21' : {'cod': '5', 'name': 'Utilizar os conhecimentos históricos para compreender e valorizar os fundamentos da cidadania e da democracia, favorecendo uma atuação consciente do indivíduo na sociedade.'},
                '22' : {'cod': '5', 'name': 'Utilizar os conhecimentos históricos para compreender e valorizar os fundamentos da cidadania e da democracia, favorecendo uma atuação consciente do indivíduo na sociedade.'},
                '23' : {'cod': '5', 'name': 'Utilizar os conhecimentos históricos para compreender e valorizar os fundamentos da cidadania e da democracia, favorecendo uma atuação consciente do indivíduo na sociedade.'},
                '24' : {'cod': '5', 'name': 'Utilizar os conhecimentos históricos para compreender e valorizar os fundamentos da cidadania e da democracia, favorecendo uma atuação consciente do indivíduo na sociedade.'},
                '25' : {'cod': '5', 'name': 'Utilizar os conhecimentos históricos para compreender e valorizar os fundamentos da cidadania e da democracia, favorecendo uma atuação consciente do indivíduo na sociedade.'},
                '26' : {'cod': '6', 'name': 'Compreender a sociedade e a natureza, reconhecendo suas interações no espaço em diferentes contextos históricos e geográficos.'},
                '27' : {'cod': '6', 'name': 'Compreender a sociedade e a natureza, reconhecendo suas interações no espaço em diferentes contextos históricos e geográficos.'},
                '28' : {'cod': '6', 'name': 'Compreender a sociedade e a natureza, reconhecendo suas interações no espaço em diferentes contextos históricos e geográficos.'},
                '29' : {'cod': '6', 'name': 'Compreender a sociedade e a natureza, reconhecendo suas interações no espaço em diferentes contextos históricos e geográficos.'},
                '30' : {'cod': '6', 'name': 'Compreender a sociedade e a natureza, reconhecendo suas interações no espaço em diferentes contextos históricos e geográficos.'},
            }
        }
    def __init__(self, table_cod_provas, path):
        self.table_cod_provas = table_cod_provas
        self.path = path        
        
    def get_info_question(self, num_question, area):
        area_dic = self.convert_area(area)
        cod = self.table_cod_provas[area_dic['value']]
        result = self.get_data_csv(cod, num_question)
        hab = self.hab_table[area_dic['value']][result['hab']]
        return {'answer':result['gab'], 'rating': result['dif'], 'ability': hab['cod'], 'area': area_dic['value']}
    
    def get_data_csv(self, cod, num_question):
        with open(self.path, "r") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")
            # Pula a primeira linha que contém os nomes das colunas
            next(leitor)
            # Percorre as linhas restantes do arquivo
            min = None
            max = None
            for linha in leitor:
                value = 0
                try:
                    value = float(linha[8])
                except:
                    continue
                
                if linha[12] == '1' or linha[13] == '1':
                    continue

                # Verifica se o valor da coluna cod é igual a 1007
                if linha[11] == cod and linha[0] == num_question:
                    # Imprime os valores das colunas gab e nota dessa linha
                    result = {'gab': linha[3], 'hab': linha[4], 'dif': value}
                
                if min == None or min > value:
                    min = value
                    
                if max == None or max < value:
                    max = value
        result['dif'] = self.convert_to_rating(result['dif'], max, min)
        return result
    
    def convert_to_rating(self, dif, max, min):
        rating_max = 3500
        rating_min = 0
        coef = (dif - min)/(max - min)
        return coef * rating_max
                      
        
    def convert_area(self, area):
        table = {
                    'ciências da natureza e suas tecnologias': 'CN',
                    'matemática e suas tecnologias': 'MT',
                    'linguagens e códigos e suas tecnologias':'LC',
                    'ciências humanas e suas tecnologias':'CH'
                }
        value = area.lower().strip()
        keys = list(table.keys())
        similar = difflib.get_close_matches(value, keys)[0]
        return {'key': similar, 'value': table[similar]}
