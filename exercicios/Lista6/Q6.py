""" 6. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
vezes cada letra do alfabeto aparece dentro do arquivo.
 """
arq=input("Informe o caminho do arquivo: ") #CursoUdemyPython/exercicios/Lista6/arq.txt
arquivo=open(arq)
texto=arquivo.read()
a=0
for c in texto:
    if(c!=' '):
        a+=1
print(a)