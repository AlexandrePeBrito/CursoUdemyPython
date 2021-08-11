#ARRAY EM C/JAVA eh preciso estipular o numero max de elementos e selecionar o tipo.


#ARRAY EM PYTHO não possui tamanho fixo. Nem um tipo fixo.


#Exemplo de lista
#lista = [1,2,5,7,9,12,52,4,11,3,97,67,23,2,18,2,1,9,2,53,25,64,2]

#lista2 = ["s","a","l","v","a","d","o","r"]

#lista3 = [2,'a',5,'e']

#lista4 = [list(range(2,13))]

#print(lista)
#print(lista2)
#print(lista3)
#print(lista4)

#print("\n\n")

#Verificando um valor na lista usando IF
#num=1
#if num in lista3:
#    print(f"Achei o {num}")
#else:
#    print(f"Não achei")

#invertendo listas
#lista.reverse()     
#lista2.reverse()

#Ordenando Listas
#lista.sort()     
#lista2.sort()

#print(lista)
#print(lista2)

#Verificando Numeros da lista
#print(sum(lista))
#print(min(lista))
#print(max(lista))
#print(len(lista))


#Verificando a ocorrencia de valor na lista
#print(lista.count(2))
#print(lista.count(6))
#print(lista2.count("a"))

#Adicionando elemento nas listas
#lista5 = [42,1]
#print(lista5)
#lista5.append(5)         #Adiciona 1 elemento por vez
#print(lista5)

#lista5.append([74,6,8])     #Adiciona um tipo vetor ao vetor
#print(lista5)

#lista5.extend([248,624,1,3,8,9])   #Adiciona os elementos do vetor no vetor.
#print(lista5)

#Podemos adicionar elementos em um lugar especifico
#lista5.insert(4,999)
#print(lista5)

#verificar o tamanho da lista
#print(len(lista5))

#removendo elementos
#lista5.pop()   #removendo ultimo elemento
#lista5.pop(3)  #removendo no indice

#Apagar a lista toda
#lista5.clear()

#encontrando o indice de um elemento
#lista5.index(2)      #encontrar o indice do elemento 2

#convertendo String em lista

lista7 = "O parágrafo se inicia com uma margem no canto esquerdo da página."
lista8 =  "em,sua,primeira,linha"
lista9 = ", indicando o começo, e se encerra com um ponto final, após o qual não há mais texto, a não ser na linha posterior com o recuo de margem, indicando o início de um novo parágrafo. Assim, todas as partes do texto estruturadas da seguinte maneira podem ser consideradas um parágrafo."
print(lista7)
lista7 = lista7.split()     #separa os elementos pelos espaços entre elas
print(lista7)

#print(lista8)
lista8 = lista8.split(',') #separa os elementos pelo parametro
#print(lista8)

#convertendo Lista em String 
#frase = " ".join(lista7)
#print(frase)

