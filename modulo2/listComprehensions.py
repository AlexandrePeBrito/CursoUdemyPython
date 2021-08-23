#Utilizamos list comprehension para gerar listas de dados processados
#
#Sintaxe
#[dado for dado in iteravel]

#exemplos
numeros=[1,2,3,4,5]
#res=[ numero * 10 for numero in numeros]
#print(res)

#dividindo a expresao
#-Primeira parte: for numero in numeros
#-Segudna parte: numero *10

#exemplos

#res=[numero/2 for numero in numeros]
#print(res)
#def funcao(numero):
#    numero=numero*numero
#    return numero

#res=[funcao(numero) for numero in numeros]
#print(res)

res=[ numero * 2 for numero in numeros]
print(res)

#faz a mesma coisa que o de cima
num_drobrados=[]
for numero in numeros:
    num_drob=numero*2
    num_drobrados.append(num_drob)

print(num_drobrados)