#Leia um valor em real e cotação do dolar. Em seguida,
#Imprima o valor correspondente em dolares.

real=float(input("Informe um valor: "))
cotacao=float(input("Informe a cotaçao do dolar: "))

dolar=real*cotacao

print(f"O valor correspondente de dolar eh {round(dolar,1)}")