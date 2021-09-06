""" 9. Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com
o conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do
segundo).
"""

arq1=input("Informe o caminho do arquivo: ")#'CursoUdemyPython/exercicios/Lista6/arq.txt'
arq2=input("Informe o caminho do arquivo: ")#'CursoUdemyPython/exercicios/Lista6/novo.txt'
arquivo1=open(arq1)
arquivo2=open(arq2)
arquivo3=open('CursoUdemyPython/exercicios/Lista6/novoDoNovo.txt','w')
texto=arquivo1.read()
arquivo3.write(texto)
texto=arquivo2.read()
arquivo3.write(texto)

