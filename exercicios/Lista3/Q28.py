#Faça um programa que leia um valor N inteiro e positivo,
#calcule o mostre o valor E, conforme a fórmula a seguir
#E=1+1/1!+1/2!+1/3!+...+1/N!

valores=[]
n=int(input("Informe um numero: "))
valores.append(1)
n_fat=1
if(n>0):
    for c in range(1,n+1):
        for i in range(1,c+1):
            n_fat = n_fat * i 
        valores.append(1/n_fat)
    print(valores)
    print(f"E = {sum(valores)}")
else:
    print("valor invalido")
