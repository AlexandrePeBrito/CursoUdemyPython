#4. Faça uma função para veríficar se um número é um quadrado perfeito. Um quadrado
#perfeito é um número inteiro não negativo que pode ser expresso como o quadrado de
#outro número inteiro. Ex: 1,4,9...
import math
def verfQuadradoPerf(num):
    if(math.sqrt(num)-int(math.sqrt(num))):
        print(math.sqrt(num))
        print(int(math.sqrt(num)))
        print("Numero não eh um quadrado perfeito")
    else:
        print(math.sqrt(num))
        print(int(math.sqrt(num)))
        print("Numero eh um quadrado perfeito")

n=int(input("Informe um numero: "))
verfQuadradoPerf(n)