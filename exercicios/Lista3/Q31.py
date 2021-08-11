#Faça um programa que calcule e escreva o valor de S
# S=1/1+3/2+5/3+7/4...99/50
u=1
valores=[]
for c in range(1,100):
    if(c%2==1):
        valores.append(round(c/u,2))
        u+=1
print(valores)
print(f"S = {sum(valores)}")

