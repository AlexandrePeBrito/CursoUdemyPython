#Leia um número positivo do usuário, então, calcule e 
#imprima a sequência Fibonacci até 0 primeiro número 
#superior ao número lido. Exemplo: se o usuário informou 
#o número 30, a sequência a ser impressa será 
#0 1 1 2 3 5 8 13 21 34
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

print(fibo)

