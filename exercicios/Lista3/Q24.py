#Escreva um programa que leia um número inteiro e calcule a
#soma de todos os divisores desse número, com exceção dele
#próprio. Ex: a soma dos divisores do número 66 é
#1+2+3+6+11+22+33=78
divisores=[]
texto=[]
n=int(input("Informe um numero: "))
txt='1 '
i=0
texto.append(txt)
divisores.append(1)
for c in range(2,n):
    if(n%c==0):
        i+=1
        divisores.append(c)
        txt=f'+ {c} '
        texto.append(txt)
print(f'A soma dos divisores eh {sum(divisores)} = {texto}')