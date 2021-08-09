#Leia uma temperatura em graus celsius e apresente-a convertida em fahrenheit.
# A formula da conversao eh: C=5*(F-32)/9,
# sendo F a temperatura em fahrenheit e c a temperatura em celsius.

F=float(input("Informe a temperatura em Fahrenheit: "))

C=5*(F-32)/9
print(f"A temperatura em Celsius eh {round(C,1)}")