# MAP - Com o MAP fazemos mapeamento de valores para função 
#Obs: MAP so eh possivel visualzar uma vez

import math
raios=[2,4,1,5,7,8,2]

def area(r):
    return math.pi*(pow(r,2))

#print(area(2))

#Exemplo comum
areas=[]
for r in raios:
    areas.append(area(r))
#print(areas)

#Exemplo usando MAP
areasMap = map(area, raios)
#print(list(areasMap))           #Forma de imprimir um MAP


#Exemplo de MAP com Lambda
#area= lambda r: math.pi*(pow(r,2))
#areasMap1 = map(area,raios)

#print(list(map(lambda r: math.pi*(pow(r,2)),raios)))

cidades=[('salvador',29),('Rio de janeiro',45),('Berlim',10),('Sao paulo',22),('catu',32)]
print(cidades)
#converter em Farehnheit]
c_para_f=lambda dado: (dado[0], (9/5) * dado[1]+32)

print(list(map(c_para_f,cidades)))