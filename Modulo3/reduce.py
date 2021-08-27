#Reduce deixou de ser uma função integrada entao temos que chamar importando functools
#recebe 2 parametros, Função e iteravel

#So utilize reduce se for necessariamente precisa dela. Seria melhor utilizar um  loop FOR

#Para entender o reduce:

#imagine uma coleção de dados:
# Dados = a1,a2,a3,a4,a5...an
#e voce tem  uma função   que recebe dois parametros:
#def function (x,y):
#   return x*y

#A função reduce funciona da seguinte forma
#PASSO 1 -> res1= f(a1,a2)    #aplica a função nos 2 primeiros elementos e guarda o resultado
#PASSO 2 -> res2= f(res1,a3)    #aplica a função com o resultado anterior e o prox elemento
#PASSO 3 -> res3= f(res2,a4)    #ele ira fazer o resultado do passo anterior com o elemento do proximo passo
#PASSO N -> resM= f(resn,an)    

#Outra representação seria:
#funcao(funcao(funcao(funcao(funcao(a1,a2),a3),a4),a5),a6)

from functools import reduce
dados=[2,4,3,8,5,4,7,9,6,1]

#usando REDUCE
aux = lambda x,y: x*y
prod=reduce(aux,dados)
print(prod)

#Usando for
prod1=1
for n in dados:
    prod1=prod1*n
print(prod1)
