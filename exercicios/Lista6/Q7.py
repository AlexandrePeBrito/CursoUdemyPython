""" 7. Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto
contendo o texto do arquivo de entrada, mas com as vogais substituídas por ". """
arquivo=open('CursoUdemyPython/exercicios/Lista6/arq.txt')
arquivo1=open('CursoUdemyPython/exercicios/Lista6/novo.txt','w') 
texto=arquivo.read()
for c in texto:
    if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        arquivo1.write('.')
    else:
        arquivo1.write(c)