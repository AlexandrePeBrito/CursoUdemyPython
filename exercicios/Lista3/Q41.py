#Faça um programa que calcula a associação em paralelo de 
#dois resistores R1 e R2 fornecidos pelo usuário via teclado.
#O programa fica pedindo estes valores e calculando até que
#o usuário entre com um valor para resistência igual a zero.

#R=(r1*r2)/(r1+r2)
R=0
while(R!=1):
    r1=int(input("Informe um valor: "))
    r2=int(input("Informe um valor: "))

    R=(r1*r2)/(r1+r2)

