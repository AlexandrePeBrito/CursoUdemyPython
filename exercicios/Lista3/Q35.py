#Faça um programa que some os números impares contidos em um
#intervalo definido pelo usuário. O usuário define o valor
#inicial do intervalo e o valor final deste intervalo e o
#programa deve somar todos os números ímpares contidos neste
#intervalo. Caso o usuário digite um intervalo inválido 
#(começando por um valor maior que o valor final) deve ser
#escrito uma mensagem de erro na tela, “Intervalo de valores
#inválido” e o programa termina. Exemplo de tela de saída:
#Digite o valor inicial e valor final: 5 
# 10 
#Soma dos ímpares neste intervalo: 21
valores=[]
inicio=int(input("Informe o numero inicial: "))
final=int(input("Informe o numero Final: "))

if(inicio<final):
    for c in range(inicio,final+1):
        if(c%2==1):
            valores.append(c)
    print(f"Soma dos ímpares neste intervalo: {sum(valores)}")
else:
    print("Intervalo invalido!")
    