#Faça um programa que some os termos de valor par da 
#sequência de Fibonacci, cujos valores não ultrapassem 
#quatro milhões.
par=[]
fibo=[]
num=int(input("Informe um numero: "))
fibo.append(0)
fibo.append(1)
c=2
var=0
while(var<=num):
    var=fibo[c-1]+fibo[c-2]
    fibo.append(var)
    c+=1

for c in range(0,len(fibo)):
    if(fibo[c]%2==0 and fibo[c]<4000000):
        par.append(fibo[c])
print(par)