#10. Faça uma função que receba dois números e retorne qual deles é o maior.

def comparar(n1,n2):
    if(n1>n2):
        return n1
    elif(n2>n1):
        return n2
    elif(n1==n2):
        return 0
num1=int(input("Informe um numero: "))
num2=int(input("Informe um numero: "))
resp=comparar(num1,num2)

if(resp==0):
    print("Os numeros sao iguais!")
else:
    print(f"O maior numero eh {resp}")