#Dados n e dois números inteiros positivos, i e j, diferentes
#de 0, imprimir em ordem crescente os n primeiros naturais
#que são múltiplos de i ou de j e ou de ambos. Exemplo:
#Para n=6, i=2 e j=3 a saída deverá ser: 0,2,3,4,6,8.

n=int(input("Informe um numero de N: "))
i=int(input("Informe um numero: "))
j=int(input("Informe um numero: "))
if(i!=0 and j!= 0):
    for c in range(1,int(n/2)+1):
        print(c*i)
        print(c*j)