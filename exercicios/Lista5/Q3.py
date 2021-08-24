#3. Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor
#de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.
def verificaNumero(numero):
    if(numero<0):
        return -1
    elif(numero>0):
        return 1
    elif(numero==0):
        return 0
n=int(input("Informe um numero: "))
f=verificaNumero(n)
if(f==1):
    print("O numero inserido eh positivo")
elif(f==-1):
    print("O numero inserido eh negativo")
elif(f==0):
    print("O numero eh Igual a 0")