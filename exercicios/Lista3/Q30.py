#Faça programas para calcular as seguintes sequências:
#1+2+3+4+5+...+n
#1-2+3-4+5+..+(2n-1)
#1+3+5+7+..+(2n-1)

n=int(input("Informe um numero inteiro: "))
valores=[]
for c in range(1,n+1):
    valores.append(c)
print(f"A soma eh {sum(valores)}")
valores.clear()
for c in range(2*n,1,-1):
    valores.append(c-(c-1))
print(f"A soma eh {sum(valores)}")
valores.clear()
for c in range(1,2*n):
    if(c%2==1):
        valores.append(c)
print(f"A soma eh {sum(valores)}")