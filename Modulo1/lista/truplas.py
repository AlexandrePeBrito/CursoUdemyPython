#Tuplas são imutaveis e sao representadas por ()


# tupla1 =(1,2,3,4,5,6,87,2,3,4)
#print(tupla1)
#print(type(tupla1))


# tupla2 = 1,6,12,5,3,23              #Isso tambem sao uma tupla
#print(tupla2)
#print(type(tupla2))


#tupla3 = (2)                        #Nao eh uma tupla
#print(tupla3)
#print(type(tupla3))

#tupla4= (4,)                        #Isto eh uma tupla
#print(tupla4)
#print(type(tupla4))
# TUPLA eh definida pela VIRGULAnao pelo PARENTESES


#DEsempacotamento de tuplas
#tupla = ("geek university","curso completo de python")

#escola, curso = tupla                       #tem que desempacotar a tupla em variaveis correspondentes ao numero de elementos

#print(curso)
#print(escola)

#Calculo com tuplas so ocorre se todos elementos forem do memso tipo (inteiro ou real)

#tupla5=2,5,1,3,4,"s"       #ERROR
#tupla5= 5,7,9,2,1,6

#print(sum(tupla5))
#print(min(tupla5))
#print(max(tupla5))
#print(len(tupla5))


#exceção do tamanho
#tupla6="a","f","e","c","a","s"
#print(tupla6)
#print(len(tupla6))

#Contatenação de tupla
#tupla7 = 5,1,4
#tupla8 = 4,9,6,3
#tupla9 = tupla7+tupla8

#print(tupla7)
#print(tupla8)
#print(tupla9)

#contando um elemento na tupla

#tupla10 = 1,5,1,4,1,2,36,6,4,7,9
#print(tupla10.count(1))

#DICAS DE TUPLAS: Usar quando não for necessario modificar os dados contidos

meses = 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'

print(meses)
print(meses[9])