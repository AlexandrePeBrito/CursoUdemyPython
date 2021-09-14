""" 
Escrevendo em arquivos CSV - 
reader() (leitor); writer() (escritor)

writerow() -> Escreve uma linha
"""
from csv import writer

with open('CursoUdemyPython/Modulo9/filmes.csv','w') as arquivo:
    escritor_csv=writer(arquivo)
    filme= None
    escritor_csv.writerow(['Titulo','Genero','Duracao'])
    while filme!='sair':
        filme=input("Informe o nome do filme: ")
        if filme!='sair':
            genero=input("Informe o genero: ")
            duracao=input("Informe a duração: ")
            escritor_csv.writerow([filme,genero,duracao])


