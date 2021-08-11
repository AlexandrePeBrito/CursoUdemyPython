#Faça um programa que receba dois números. Calcule e mostre:
#*A soma dos números pares desse intervalo de números, 
#incluindo os números digitados;
#*A multiplicação dos números ímpares desse intervalo, 
#incluindo os digitados;
valores=[]
soma=0
prod=1
for c in range(0,2):
    n=int(input("Informe um numero: "))
    valores.append(n)
for c in range(min(valores)+1,max(valores)):
    print(c)
    if(c%2==0):
        soma=c+soma
    else:
        prod=c*prod
print(f"A soma dos numeros pares eh {soma} e\
 o produto eh {prod}")