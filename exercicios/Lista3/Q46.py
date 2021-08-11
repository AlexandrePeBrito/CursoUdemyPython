#Faça um programa que gera um número aleatório de 1 a 1000. 
#O usuário deve tentar acertar qual o número foi gerado, a 
#cada tentativa o programa deverá informar se o chute é menor
#ou maior que o número gerado. O programa acaba quando o 
#usuário acerta o número gerado. O programa deve informar
#em quantas tentativas o número foi descoberto.
import random
ale=random.randint(1,1000)
n=int(input("Chute um numero:"))

while(n!=ale):
    if(n<ale):
        n=int(input("Chute um numero mais Alto:"))

    elif(n>ale):
        n=int(input("Chute um numero mais Baixo:"))
print(f"\nVoce Acertou!! O numero era {n}")