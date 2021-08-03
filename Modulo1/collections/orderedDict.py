# Modulo Collection -> Ordered Dict

#Ordered Dict -> nos garante a ordem de inserção

from collections import OrderedDict

#dicionario = OrderedDict({'a':1,'b':2,'d':3,'c':4})

#for chave, valor in dicionario.items():
#    print(f'Chave: {chave} e valor: {valor}')

#Diferença de dict para ordere dict

#dict comum

dict1 = {'a':1,'b':2}
dict2 = {'b':2,'a':1}

print(dict1 == dict2)   #true


#Ordered dict 

dict3 = OrderedDict({'a':1,'b':2})
dict4 = OrderedDict({'b':2,'a':1})

print(dict3 == dict4)   #false