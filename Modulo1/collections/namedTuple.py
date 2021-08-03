# Modulo Collection -> Named Tuple

#Named Tuple -> sao tuples onde diferenciamos nomes para as mesma e parametros

tupla = (1,2,3)
#print(tupla[1])

from collections import namedtuple


#declaração de namedTuple

#modelo 1
cachorro = namedtuple('cachorro','idade raca nome')     

#modelo 2
cachorro1 = namedtuple('cachorro','idade, raca, nome') 

#modelo 3
cachorro2 = namedtuple('cachorro',['idade','raca','nome']) 


#utilizando

Zelda = cachorro(idade=3,raca='viralata', nome='Zelda')

print(Zelda)

#Acessando

#modelo 1
print(Zelda[0])
print(Zelda[1])
print(Zelda[2])

#modelo 2
print(Zelda.idade)
print(Zelda.raca)
print(Zelda.nome)



