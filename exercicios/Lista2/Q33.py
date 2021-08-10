#Um produto vai sofrer aumento de acordo com a tabela abaixo. 
#Leia o preço antigo, calcule e escreva o preço novo, e 
#escreva uma mensagem em função do preço novo (de acordo com 
#a segunda tabela).
#PREÇO ANTIGO PERCENTUAL DE AUMENTO

#Preço antigo         | Percentual de Aumento
#até R$ 50            |     5%
#entre R$ 50 e R$ 100 |     10%
#acima de R$ 100      |     15%


#Preço novo                   |  Mensagem
#até R$ 80                    |  Barato
#entre R$ 80 e R$ 120         |  Normal
#acima de R$ 120 e R$ 200     |  Caro
#acima de R$ 200              | Muito Caro

preco_antigo=float(input("Informe o preço antigo: "))

if(preco_antigo<=50):
    preco_novo=preco_antigo*1.05
elif(50<preco_antigo<=100):
    preco_novo=preco_antigo*1.1
elif(preco_antigo>100):
    preco_novo=preco_antigo*1.15

if(preco_novo<=80):
    print(preco_novo)
    print("Barato")
elif(80<preco_novo<=120):
    print(preco_novo)
    print("Normal")
elif(120<preco_novo<=200):
    print(preco_novo)
    print("Caro")
elif(preco_novo>200):
    print(preco_novo)
    print("Muito Caro")
