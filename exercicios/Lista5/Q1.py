#1. Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro.

def dobro(num):
    return num*2
n=int(input("Informe um numero: "))
d=dobro(n)
print(f"O dobro de {n} eh {d}")