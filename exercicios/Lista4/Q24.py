#Faça um programa que leia dez conjuntos de dois valores, o
#primeiro representando o número do aluno e o segundo 
#representando a sua altura em metros. Encontre o aluno mais
#baixo e o mais alto. Mostre o número do aluno mais baixo e
#do mais alto, juntamente com suas alturas.
escola={}
menor=[]
maior=[]
for c in range(0,10):
    n= float(input("Informe a altura do aluno: "))
    escola[c]=n
menor.append(0)
menor.append(escola[0])
maior.append(0)
maior.append(escola[0])
for c in range(0,10):
    if(escola[c]>maior[1]):
        maior[1]=escola[c]
        maior[0]=c
    if(escola[c]<menor[1]):
        menor[1]=escola[c]
        menor[0]=c
print(f"O codigo do maior aluno eh {maior[0]} medindo {maior[1]} m")
print(f"O codigo do menor aluno eh {menor[0]} medindo {menor[1]} m")
