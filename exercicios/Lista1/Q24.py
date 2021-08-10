#Leia um valor de area em metros quadrados m2 e apresente-o convertido em acres.
#A formula de conversao eh: A=M*0.000247,
#sendo M a area em metros quadrados a A area em acres.

m=float(input("Informe a area em metros quadrados: "))

a=m*0.000247

print(f"A area convertida em acres eh {round(a,2)}")