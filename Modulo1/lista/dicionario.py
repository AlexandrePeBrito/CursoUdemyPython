#DICIONARIOS Sao representados por {} e não tem chaves repetidas

paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'esp':'Espanha'}
print(paises)

#Acessando o dicionario
#modelo 1
print(paises['br'])              #Para acessar um dicionario vc precisar acessar sua chave
#print(paises['ru'])             #Caso tenha um acesso que nao existe dara um ERROR

#modelo 2
print(paises.get('br'))
print(paises.get('ru'))            #Caso tenha um acesso que nao existe NAO dara ERROR mas dara como NONE

#Exemplo

pais1 = paises.get('ru','Nao encontrado')  #Caso identifique o codigo RU ira trazer o seu conteudo, caso seja None trará a mensagem alternativa
pais2 = paises.get('eua','Nao encontrado')

print(pais1)
print(pais2)

#Adicionando elemento
#modelo 1
paises['ru'] = 'RUSSIA'

print(paises)

#modelo 2
novoPais = {'uru':'Uruguai'}
paises.update(novoPais)
print(paises)


#removendo elemento
#modelo 1
ref= paises.pop('uru')          #Essa ação retorna o valor contido no codigo removido
print(paises)

#modelo 2
del paises['ru']

print(paises)

#Copiando dicionario
#modelo 1
novo=paises.copy()
print(novo)
#modelo 2
novo1=paises
print(novo1)
#limpando dicionario

paises.clear()

print(paises)

