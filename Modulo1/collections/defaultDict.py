# Modulo Collection -> Default Dict

#Default Dict ->Ao fazer chamada de uma chave inexistente, não ocorrera erro. Criar um dicionario usando o 
# default dict informamos um valor default ou lambda que ira ser utilizada sempre que não houver um valor definido.
# E caso solicite acesso a um item inexistente sera criada uma chave default.


#Exemplo de dicionario
#dicionario = {1:'Alexandre Brito'}      
#print(dicionario)                       
#print(dicionario[1])

from collections import defaultdict

dicionario = defaultdict(lambda:0)

print(dicionario)
dicionario['nome'] = 'alexandre'
print(dicionario)

print(dicionario['sexo'])
print(dicionario)