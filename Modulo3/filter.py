# FILTER - Serve para filtrar dados de uma coleção
#filter recebe 2 parametros um, uma função e um iteravel
#Obs: Filter so eh possivel visualzar uma vez

import statistics   #biblioteca para dados estatisticos

dados = 1.63,2.8,3.1,4,5.9,6.5
media=statistics.mean(dados)            #calculando media

resp = filter(lambda x: x>media , dados)    #ele ira salvar no RESP todos os elementos de DADOS que eh maior que a media
#print(list(resp))

paises=['','Brasil','','','Argentina','Peru','Chile','Equador','','Eua','Canada','China']
#print(paises)
res=filter(lambda x: x!='',paises)
res1=filter(None,paises)
#print(list(res))
#print(list(res1))

#Exemplo mais complexo
usuarios=[
    {'username':'alexandre','tweets':['Eu adoro cafe','Fora Bolsonaro','Vamos Bahia']},
    {'username':'maiure','tweets':['Eu adoro bolo']},
    {'username':'joselito','tweets':['Eu adoro macarrao','Vamos Bahia']},
    {'username':'ana maria','tweets':[]}
]

res=filter(lambda usuario: len(usuario['tweets'])!=0,usuarios)
#forma 1
inativos=filter(lambda usuario: len(usuario['tweets'])==0,usuarios)
#print(list(inativos))

#forma 2
inativos=filter(lambda usuario: not usuario['tweets'],usuarios) #uma lista vazia representa FALSE
##print(list(inativos))



#combinando  MAP com FIlter

instrutora = ['maiure','ana','carla','maria']

lista = map(lambda nome: f"Sua instrutora eh {nome}", filter(lambda nome: len(nome)>=5,instrutora))
print(list(lista))