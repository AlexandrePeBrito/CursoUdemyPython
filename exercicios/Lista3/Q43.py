#Faça um programa que leia um número indeterminado de idades
#de indivíduos (pare quando for informada a idade 0), e
#calcule a idade média desse grupo.
idade=int(input("Informe a idade: "))
grupo=[]
c=0
while(idade!=0):
    c+=1
    grupo.append(idade)
    idade=int(input("Informe a idade: "))
media=sum(grupo)/c
print(f"A media das idades eh {round(media,1)}")
