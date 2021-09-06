""" 5. Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre na tela
quantas vezes aquele caractere ocorre dentro do arquivo.
 """
arquivo=open('CursoUdemyPython/exercicios/Lista6/arq.txt')
texto=arquivo.read()
carac=input('Informe um caractere: ')
ca=0
for c in texto:
    if(c == carac):
        ca+=1
arquivo.close()

print(f"Foi identificado {ca} deste caractere")
