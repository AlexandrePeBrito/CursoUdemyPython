#faça leitura de tres valores e apresente como resultado a soma dos quadrados dos tres valores lido

valores=[]
for c in range(0,3):
    num=int(input("Informe um valor: "))
    valores.append(num)

print(f"A soma dos valores sao {sum(valores)}")