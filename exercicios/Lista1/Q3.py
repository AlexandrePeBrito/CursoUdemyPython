#peça ao usuario para digitar 3 valores inteiros e imprima a soma deles

valores=[]
for c in range(0,3):
    num=int(input("Informe um numero inteiro: "))
    valores.append(num)
print(sum(valores))