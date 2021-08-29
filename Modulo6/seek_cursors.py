#Função seek eh utilizada para movimentar o cursor no artigo,
#recebe um parametro que eh o local para o cursor se deslocar

#Movimentando o cursor
""" arquivo.seek(0)
print(arquivo.read())
arquivo.seek(14)
print(arquivo.read()) """

#Ler uma linha
""" arquivo = open("CursoUdemyPython/Modulo6/test.txt")
ret=arquivo.readline()
print(ret.split(' ')) """

#Ler todas as linhas colocando em uma lista
arquivo = open("CursoUdemyPython/Modulo6/test.txt")
linhas=arquivo.readlines()
print(linhas)
print(len(linhas))

arquivo.close()
