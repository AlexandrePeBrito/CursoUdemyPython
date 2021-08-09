#Leia uma temperatura em graus Celsius e apresente-a convertida em Kelvin.
# A formula da conversao eh: K=C+273.15,
# sendo K a temperatura em Kelvin e c a temperatura em celsius.

C=float(input("Informe a temperatura em Celsius: "))

K=C+273.15
print(f"A temperatura em Kelvin eh {round(K,1)}")