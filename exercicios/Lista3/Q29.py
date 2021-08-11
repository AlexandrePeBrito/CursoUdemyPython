#Escreva um programa para calcular o valor da série, para 
#5 termos.
# S=0+1/2!+2/4!+3/6!+..

valores=[]
n_fat=1
u=2
for c in range(1,6):
    for i in range(1,u):
        n_fat = n_fat * i 
    valores.append(c/n_fat)
    u+=2
print(f"S = {round(sum(valores),2)}")
