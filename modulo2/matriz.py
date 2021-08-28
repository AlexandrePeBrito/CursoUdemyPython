#python n tem arrays, tem listas

#vamos ver as listas aninhadas que correspodem a Matrizes

#representa uma matriz 3x3
lista=[[1,2,3],[4,5,6],[7,8,9,]]

#Acesso de dados

#print(lista[0])     #acessa a primeira lista
#print(lista[0][1])  #Acessando o 2 elemento da lista 1


#metodos de acesso e iteração da matriz
#for l in lista:
#    for num in l:
#        print(num)

[[print(num) for num in l ] for l in lista]