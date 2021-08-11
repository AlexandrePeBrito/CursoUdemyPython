#Faça um programa que calcule o maior número palíndromo 
#feito a partir do produto de dois números de 3 dígitos. 
#Ex: O maior palíndromo feito a partir do produto de dois
#números de dois dígitos é 9009 = 91*99.

for c in range(100,1000):
    for i in range(100,1000):
        teste=c*i
        teste=str(teste)
        if(len(teste)==5):
            if(teste[0]==teste[4] and teste[1]==teste[3]):
                n1=c
                n2=i
                pal=int(teste)
        elif(len(teste)==6):
            if(teste[0]==teste[5] and teste[1]==teste[4] and teste[2]==teste[3]):
                n1=c
                n2=i
                pal=int(teste)
print(f"{n1} * {n2} = {pal}")