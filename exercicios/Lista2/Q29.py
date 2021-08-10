#Faça uma prova de matemática para crianças que estão 
#aprendendo a somar números inteiros menores do que 100. 
#Escolha números aleatórios entre 1 e 100, e mostre na tela 
#a pergunta: qual é a soma de a + b, onde a e b são os 
#números aleatórios. Peça a resposta. Faça cinco perguntas 
#ao aluno, e mostre para ele as perguntas e as respostas
#corretas, além de quantas vezes o aluno acertou.
import random

n1=random.randint(1,100)
n2=random.randint(1,100)

resp=int(input(f"Qual a soma entre {n1} e {n2}? "))
if(resp==(n1+n2)):
    print("Voce Acertou")
else:
    print("Voce errou")
