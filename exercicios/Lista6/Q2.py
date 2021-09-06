""" 2. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
linhas esse arquivo possui.
 """

arquivo = open("CursoUdemyPython/exercicios/Lista6/arq.txt")
linhas=arquivo.readlines()                              #gera uma lista com cada bloco uma linha
print(len(linhas))
arquivo.close()