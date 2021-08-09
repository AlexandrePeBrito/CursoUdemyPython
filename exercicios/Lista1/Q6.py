#Leia uma temperatura em graus celsius e apresente-a convertida em fahrenheit.
# A formula da conversao eh: F=C*(9/5)+32,
# sendo F a temperatura em fahrenheit e c a temperatura em celsius.

C=float(input("Informe a temperatura em Celsius: "))

F=C*(9/5)+32
print(f"A temperatura em Fahrenheit eh {round(F,1)}")