#Faça um programa que some os números primos existentes 
#entre a e b, onde a e b são números informados pelo usuário.
a=int(input("Informe o inicio do intervalo: "))
b=int(input("Informe o final do intervalo: "))
primo=[]
for c in range(a,b+1):
    u=0
    for i in range(1,c+1):
        if(c%i==0):
            u+=1
    if(u<=2):
        primo.append(c)
print(sum(primo))