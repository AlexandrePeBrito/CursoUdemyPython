#Funções com retorno

#numeros=[1,2,4,5,9]
#n=numeros.pop()
#print(f"A função Pop() retorna o elemento removido {n}")
#print(numeros)
#ret=print()
#print(f"O retorno da função print() eh {ret}")

#Quando chama uma função em cima antes da sua definiçao, Ocorre um erro
#print(f"5 ao quadrado eh {potencia(5,2)}")
#print(f"5 ao quadrado eh {pot(5,2)}")      

#Função com retorno
def potencia(num,indice):
    for c in range(0,indice-1):
        num=num*num 
    return num

#Função sem retorno
def pot(num,indice):
    for c in range(0,indice-1):
        num=num*num
    print(num)

print(f"5 ao quadrado eh {potencia(5,2)}")
print(f"5 ao quadrado eh {pot(5,2)}")           #Função sem retorno