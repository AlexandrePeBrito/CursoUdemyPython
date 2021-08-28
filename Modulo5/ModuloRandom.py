#Modulos são outros arquivos python

#Modulo Random -> Funções para gerar numeros pseudo-aleatorio

#Forma 1 -> importar o modulo todo, não recomendavel pois vai ter todas as
#funções armazenada na memoria.
"""import random
print(random.randrange(2,19))
"""

#Forma 2 -> Importando uma função especifica
from random import randrange
print(randrange(2,19))