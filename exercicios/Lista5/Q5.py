#5. Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
#Sendo que o raio é passado por parâmetro.

#V=4/3*pi*R^3
def volEsfera(raio):
    return (4*3.14*(pow(raio,3)))/3

n=float(input('Informe o valor do raio: '))
volume=volEsfera(n)
print(volume)