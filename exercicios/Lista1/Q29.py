#leia quatro notas,
# calcule a media aritmetica e imprima o resultado

valores=[]
for c in range(0,4):
    num=int(input("Informe um valor: "))
    valores.append(num)

media=sum(valores)/4
print(f"A media dos valores sao {media}")