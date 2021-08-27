# Cria um iteravel zip object q agrega outros iteraveis

lista1=[1,5,76,3]
lista2=[0,9,5,4,3,7]

listaFinal=zip(lista1,lista2)
print(list(listaFinal))             #gera uma lista com tuplas
print(tuple(listaFinal))            #ele deleta dps do seu primeiro uso
print(dict(listaFinal))