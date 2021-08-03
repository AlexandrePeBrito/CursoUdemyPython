#Conjuntos esta relacionada a Teoria dos conjuntos na Matematica
#Conjuntos sao chamados de Sets
#-NÃO possuem valores duplicados
#-NÃO possuem valores ordenados
#-Elementos NÃO sao indexados

#Usamos conjuntos quando NÃO precisa ordenar os elementos. E NÃO precisa se preocupar com valore,chaves e itens duplicados

#Sao representados por {}

#Diferenças entre Sets e dicionarios
    #-Dicionarios possuem chaves e valores. 
    #-Sets so possuem valores

#Definindo SETS

#s ={5,7,3,1,4,2,1}  #Valores repetidos não sao contados

#print(s)

#Formas de criar Sets

#lista=[1,5,2,4,7,9,3,1,4,5,2,6,5,4,7,4]
#print(lista)
#s1=set(lista)
#print(s1)

#Formas de verificação

#if 4 in s1:
#    print("Contem")
#else:
#    print("NÃO tem")

#Listas aceitam valores duplicados
#lista = [2,14,5,3,7,9,1,2,4,7,3,5,12,4,5215,21,4465]
#print(lista)

#Tuplas aceitam valores duplicados
#tupla =(2,14,5,3,7,9,1,2,4,7,3,5,12,4,5215,21,4465)
#print(tupla)

#Dicionarios NÃO aceitam chaves duplicadas
#dicionario = {}.fromkeys([2,14,5,3,7,9,1,2,4,7,3,5,12,4,5215,21,4465],"dict")
#print(dicionario)

#Dicionarios NÃO aceitam valores duplicados
#conjunto = {2,14,5,3,7,9,1,2,4,7,3,5,12,4,5215,21,4465}
#print(conjunto)


#Podem misturar os dados nos SETS

#s= {'s',5,4.5,7,"a",True}
#print(s)

#Removendo VAlores
#modelo 1
#s.remove(5)         #Caso n seja encontrado o valor sera gerado um error
#print(s)

#modelo 2
#s.discard(4.5)        #exclui o elemento e caso n tenha n gera error
#print(s)


#Copiando Conjuntos

#modelo 1

#novo=s.copy()
#novo.add(11)         #Adicionando um elemento
#print(novo)

#Modelo 2 

#novo=s                  #Cria um clone que altera o original
#novo.add(11)
#print(novo)
#print(s)


#Limpando conjunto

#s.clear()
#print(novo)
#print(s)

#Aplicação

estudantesPython= {'alexandre','maiure',"ana",'rui','victor','leo'}
estudantesJava = {'lito','gustavo',"ana",'rui','victor','lucio','thais','atila'}

python=estudantesPython.difference(estudantesJava)             #Descobrindo qual estudante eh apenas de Python
java=estudantesJava.difference(estudantesPython)               #Descobrindo qual estudante eh apenas de Java
 

todos=estudantesPython.intersection(estudantesJava)     #Descobrindo estudantes que estudam em 2  cursos
unicos = estudantesPython.union(estudantesJava)         #Descobrindo todos os estudantes


#print(unicos)
#print(todos)
#print(python)
print(java)
