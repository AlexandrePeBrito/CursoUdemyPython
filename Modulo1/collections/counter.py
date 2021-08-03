#Modulo Collection - Counter (Contador)

#Collections -> High-performance Container Datetypes

#Counter -> Recebe um valor interavel como parametro e cria um objeto do tipo Collection Counter que 
# eh parecido com um dicionario. Contendo como chave o elemento da lista passada como parametro e como valor
# a quantidade de ocorrencias desse elemento. 

from collections import Counter

#lista = [1,2,4,5,3,1,4,52,8,7,6,1,7,5,2,4,7,8,9,5,4,1,2,6,8,3]

#res=Counter(lista)

#print(res)

#lista1 = ["alexandre",'alex','maiure','ana','lito', 'joselito']

#print(Counter(lista1))

#print(Counter("Alexandre"))             #Ele difere maiusculo de minusculo

texto = "Nos estudos sobre a poesia moderna, as estrofes são definidas como sendo cada uma das seções que constituem um poema.\
     Cada seção é composta pelo agrupamento de versos, rimados ou não, com unidade de sentido e ritmo.\
     O início e o final de cada estrofe do poema são delimitados com espaços em branco.\
 Essa estrutura revela a pausa rítmica que deve ser considerada durante a leitura do texto."
palavras= texto.split()

res= Counter(palavras)

print(res.most_common(5))           #os 5 elementos que mais aparecem

print(Counter("Nos estudos sobre a poesia moderna, as estrofes são definidas como sendo cada uma das seções que constituem um poema.\
     Cada seção é composta pelo agrupamento de versos, rimados ou não, com unidade de sentido e ritmo.\
     O início e o final de cada estrofe do poema são delimitados com espaços em branco.\
 Essa estrutura revela a pausa rítmica que deve ser considerada durante a leitura do texto."))