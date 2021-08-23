#Adicionando estruturas logicas na List comprehensions


#exemplos

numeros=[1,2,3,4,5]

pares=[numero for numero in numeros if numero%2==0]
impares=[numero for numero in numeros if numero%2==1]

print(pares)
print(impares)