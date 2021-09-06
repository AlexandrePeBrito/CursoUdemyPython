""" 8. Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo
conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas. Os no-
mes dos arquivos serão fornecidos, via teclado, pelo usuário. A função que converte
maiúscula para minúscula é o upper(). Ela é aplicada em cada caractere da string.
"""
arq=input("Informe o caminho do arquivo: ") #CursoUdemyPython/exercicios/Lista6/arq.txt
arquivo=open(arq)
arquivo2=open('CursoUdemyPython/exercicios/Lista6/novo.txt','w')
texto=arquivo.read()
for c in texto:
    if(c==c.lower()):
        arquivo2.write(c.upper())
    else:
        arquivo2.write(c)