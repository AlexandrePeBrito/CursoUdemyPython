#Leia uma temperatura em graus Celsius e apresente-a convertida em Kelvin.
# A formula da conversao eh: C=k-273.15,
# sendo K a temperatura em Kelvin e c a temperatura em celsius.

K=float(input("Informe a temperatura em Kelvin: "))

C=K-273.15
print(f"A temperatura em Celsius eh {round(C,1)}")