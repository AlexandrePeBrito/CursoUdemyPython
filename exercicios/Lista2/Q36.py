#Escreva um programa que, dado o valor da venda, imprima a 
#comissão que deverá ser paga ao vendedor. Para calcular a 
#comissão, considere a tabela abaixo:

#Venda mensal                                       |   Comissao
                                     
#Maior ou Igual a R$100.000                         |R$700 +16% das vendas
#Menor que R$100.000 e maior ou igual a R$80.000    |R$650 +14% das vendas
#Menor que R$80.000 e maior ou igual a R$60.000     |R$600 +14% das vendas
#Menor que R$60.000 e maior ou igual a R$40.000     |R$550 +14% das vendas
#Menor que R$40.000 e maior ou igual a R$20.000     |R$500 +14% das vendas
#Menor que R$20.000                                 |R$400 +14% das vendas

valor=float(input("Informe o valor da venda: "))

if(valor>=100000):
    comissao=700+(valor*0.16)
elif(80000<=valor<100000):
    comissao=650+(valor*0.14)
elif(60000<=valor<80000):
    comissao=600+(valor*0.14)
elif(40000<=valor<60000):
    comissao=550+(valor*0.14)
elif(20000<=valor<40000):
    comissao=500+(valor*0.14)
elif(valor<20000):
    comissao=400+(valor*0.14)
    
print(f"O valor da venda eh R${valor} e a comissao do funcionario eh R${comissao}")