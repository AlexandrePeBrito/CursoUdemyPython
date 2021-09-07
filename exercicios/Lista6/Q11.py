""" 11. Façaum programa no qual o usuário informa o nome do arquivo e uma palavra, e retorne
o número de vezes que aquela palavra aparece no arquivo.
 """
#arq1=input("Informe o caminho do arquivo: ")#'CursoUdemyPython/exercicios/Lista6/arq.txt'
palavra=input('Informe uma palavra: ')
arquivo=open('CursoUdemyPython/exercicios/Lista6/arq.txt')
texto=arquivo.readlines()
k=[]
for c in range(len(texto)):
       k.append(texto[c].split('-'))
print(k)
for lista in k:
    for elemento in lista:
        if(elemento==palavra):
            print('FOI')