
#Crie um programa que lê 6 valores inteiros pares e, em 
#seguida, mostre na tela os valores lidos na ordem inversa.
vetor=[]
c=0
while(c<=6):
    n=int(input("Informe um numero: "))
    if(n%2==0):
        c+=1
        vetor.append(n)
print(vetor[::-1])
