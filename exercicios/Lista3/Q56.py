#Faça um programa que calcule a soma de todos os números
#primos abaixo de dois milhões.
primo=[]
for c in range(1,2000000):
    u=0
    for i in range(1,c+1):
        if(c%i==0):
            u+=1
    if(u<=2):
        primo.append(c)
        print(c)
    