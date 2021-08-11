#Escreva um programa que leia um inteiro não negativo n e
#imprima a soma dos n primeiros números primos.
primo=[]
n=int(input("Informe um numero: "))
if(n>0):
    for c in range(1,n+1): 
        i=0
        for u in range(1,c+1):
            if(c%u==0):
                i+=1
        if(i<=2):
            print(c)
            primo.append(c)
    print(sum(primo))
