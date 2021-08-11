#Faça um programa que leia 10 inteiros positivos, ignorando 
#não positivos, e imprima sua média.

valores=[]
c=1
while(c<=10):
    n=int(input("Informe um numero: "))
    if(n>0):
        valores.append(n)
        c+=1

print(f"A somas dos valores eh {(sum(valores))/10}")
