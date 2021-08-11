#Em Matemática, o número harmônico designado por H (n) 
#define-se como sendo a soma da série harmónica:
#H(n)=1+1/2+1/3+1/4+..+1/n
#Faça um programa que leia um valor n inteiro e positivo
#e apresente o valor de H(n).
valores=[]
valores.append(1)
n=int(input("Informe um numero: "))
if(n>0):
    for c in range(2,n+1):
        valores.append(1/c)

    print(valores)
    print(f"A H({n}) = {sum(valores)}")
else:
    print("valor invalido")