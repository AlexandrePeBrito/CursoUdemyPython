#Calcule as raízes da equação de 2º grau. Lembrando que:
#x=(-b+-raiz(delta))/2a
#Onde, delta=B^2-4ac E ax^2 + bx + c =0 representa uma equação
#de 2º grau. A variável a tem que ser diferente de zero.
#Caso seja igual, imprima a mensagem “Não é equação de 
#segundo grau”.
#* Se delta < 0, não existe real. Imprima a mensagem Não 
# existe raiz.
#* Se delta =0, existe uma raiz real. Imprima a raiz e a 
# mensagem Raiz única.
#*Se delta > 0, imprima as duas raízes reais.
import math
a=int(input("Informe o termo A: "))
b=int(input("Informe o termo B: "))
c=int(input("Informe o termo C: "))

delta=(math.pow(b,2))-(4*a*c)
print(f"delta = {delta}")
if(delta<0):
    print("Nao existe raiz")
elif(delta==0):
    x1=(-b+math.sqrt(delta))/2*a
    print(f"A raiz eh {x1}")
elif(delta>0):
    x1=(-b+math.sqrt(delta))/2*a
    x2=(-b-math.sqrt(delta))/2*a
    print(f"As raizes sao {x1} e {x2}")

