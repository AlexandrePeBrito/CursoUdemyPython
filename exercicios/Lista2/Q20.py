#Dados três valores, A, B, C,, verificar se eles podem ser
#valores dos lados de um triângulo e, se forem, se é um
#triângulo escaleno, equilátero ou isóscele, considerando 
#os seguintes conceitos:
#O comprimento de cada lado de um triângulo é menor do que
#a soma dos outros dois lados.
#Chama-se equilátero o triângulo que tem três lados iguais.
#*Denominam-se isósceles o triângulo que tem o comprimento
#de dois lados iguais.
# * Recebe o nome de escaleno o triângulo que tem os três 
#lados diferentes.

a=float(input("Informe o tamanho do lado A: "))
b=float(input("Informe o tamanho do lado B: "))
c=float(input("Informe o tamanho do lado C: "))

if((a<b+c)and(b<c+a)and(c<a+b)):
    if(a==b==c):
        print("Triangulo equilatero")
    elif((a==b and a!=c)or(b==c and a!=b)or(a==c and b!=c)):
        print("Triangulo isoceles")
    elif(a!=b!=c):
        print("Triangulo escaleno")
else:
    print("Nao eh um triangulo")