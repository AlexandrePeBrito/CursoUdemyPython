#7. Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida
#em graus Fahrenheit. A fórmula de conversão é: F = C + (9.0/5.0) + 32.0, sendo F a
#temperatura em Fahrenheit e C' a temperatura em Celsius.

def convertCF(temp):
    return temp+(9/5)+32

valor=float(input("Informe a temperatura em Celsius: "))
f=convertCF(valor)
print(f"A temperatura em Fahrenheit eh {f}")