#Faca um algoritmo que encontre o primeiro múltiplo de 
#11, 13 ou 17 após um número dado

n=int(input("Informe um numero: "))
u=0
for c in range(n,100):
    for i in range(1,100):
        if(11*i==c or 13*i==c or 17*i==c):
            print(f"Primeiro multiplo {c}")
            u+=1
            break
    if(u==1):
        break