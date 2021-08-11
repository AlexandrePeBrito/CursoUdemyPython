#Faça um programa que leia vários números, calcule e mostre:
#(a) A soma dos números digitados
#(b) A quantidade de números digitados
#(c) A média dos números digitados
#(d) O maior número digitado
#(e) O menor número digitado
#(f) A média dos números pares
menu=int(input("1-Inserir\n2-Sair: "))
i=0
u=0
valores=[]
pares=[]
while(menu!=2):
    num=int(input("Informe um numero inteiro: "))
    valores.append(num)
    if(num%2==0):
        pares.append(num)
        u+=1
    i+=1

    menu=int(input("1-Inserir\n2-Sair: "))
print(f"Soma = {sum(valores)}\n\
Quantidade de numeros = {i}\n\
Media = {(sum(valores)/i)}\n\
Maior numero = {max(valores)}\n\
Menor numero = {min(valores)}\n")
if(u>0):
    print(f"Media dos numeros pares = {(sum(pares)/u)}")
