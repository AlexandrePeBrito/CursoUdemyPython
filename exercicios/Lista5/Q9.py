#9. Façaumam função que receba a altura e o raio de um cilindro circular e retorne o volume
#do cilindro. O volume de um cilindro circular é calculado por meio da seguinte fórmula:
#V =pi*raio^2 x altura, onde pi = 3.141592.
def volCilindro(raio,altura):
    return 3.1415926535*pow(raio,2)*altura

r=float(input("Informe o raio do cilindro: "))
alt=float(input("Informe a altura do cilindro: "))
volume=volCilindro(3,2)
print(volume)