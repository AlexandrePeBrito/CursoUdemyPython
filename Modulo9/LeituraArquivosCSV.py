""" 
Arquivo Csv - Comma Separeted Values 

Podemos ter separadores, exemplo : 
*por Virgula
*por Ponto-Virgula
*por espaço
"""
#forma nao ideal para trabalhar com arquivos csv
""" with open('CursoUdemyPython/Modulo9/lutadores.csv', encoding="utf8") as arquivo:
    dados=arquivo.read()
    #print(type(dados))
    dados=dados.split(',')[2:]
    print(dados) """

#Forma usual
""" from csv import reader 
with open('CursoUdemyPython/Modulo9/lutadores.csv', encoding="utf8") as arquivo:
    leito_csv=reader(arquivo)
    next(leito_csv)#vai para o proximo elemento da lista. pulando o cabeçalho
    for linha in leito_csv:
        #cada linha eh uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e tem {linha[2]} cm') """









