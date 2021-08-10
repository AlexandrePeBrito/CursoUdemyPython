#Três amigos jogaram na loteria. Caso eles ganhem,
#o prêmio deve ser repartido proorcionalmente ao 
#valor que cada deu para a realização da aposta.
#Faça um programa que leia quanto cada apostador
#investiu, o valor do prêmio, e imprima quanto cada um
#ganharia do prêmio com base no valor investido.

inv1=float(input("Informe o investimento do primeiro amigo: "))
inv2=float(input("Informe o investimento do segundo amigo: "))
inv3=float(input("Informe o investimento do terceiro amigo: "))
premio=float(input("Informe o valor do premio: "))

valor_inv=inv1+inv2+inv3

porc1=(inv1/valor_inv)
porc2=(inv2/valor_inv)
porc3=(inv3/valor_inv)

valor1=premio*porc1
valor2=premio*porc2
valor3=premio*porc3

print(f"O primeiro amigo ira receber R${round(valor1,2)}\n\
O segundo amigo ira receber R${round(valor2,2)}\n\
O terceiro amigo ira receber R${round(valor3,2)}\n")