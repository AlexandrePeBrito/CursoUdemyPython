# Nao confundir reversed com a função usada em lista reserve
# reverse so funciona em lista

# reversed funciona com qualquer iteravel

numeros=[1,2,3,4,5,6]
print(numeros)
numeros.reverse()
print(numeros)

numeros1=(1,2,3,4,5,6)
print(numeros1)
#numeros1.reverse()              #error
#print(numeros1)

print(list(reversed(numeros1)))     #retorna um objeto reversed que pode ser convertido
