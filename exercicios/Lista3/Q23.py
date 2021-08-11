#Faca um algoritmo que leia um número positivo e imprima 
#seus divisores.
n=int(input("Informe um numero: "))
for c in range(1,n):
    if(n%c==0):
        print(c)
print(n)