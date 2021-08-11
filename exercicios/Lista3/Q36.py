#Faça um programa que calcule a diferença entre a soma dos 
#quadrados dos primeiros 100 números naturais e o quadrado
#da soma. Ex: A soma dos quadrados dos dez primeiros números
#naturais é 1^2+2^2+...+10^2=385
#O quadrado da soma dos dez primeiros números naturais é,
#(1+2+..+10)^2 = 552 = 3025
#A diferença entre a soma dos quadrados dos dez primeiros
#números naturais e o quadrado da soma é 3025-385 = 2640.
r=0
for c in range(1,101):
    r=r+pow(c,2)
print(r)
resul=0
for i in range(1,101):
    resul=resul+i

print(f"{resul} = {pow(resul,2)}")
