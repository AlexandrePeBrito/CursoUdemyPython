#Leia um valor de area em acres e apresente-o convertido em metros quadrados.
#A formula de conversao eh: M=A*4048.58 ,
#sendo M a area em metros quadrados a A area em acres.

a=float(input("Informe a area em acres: "))

m=a*4048.58

print(f"A area convertida em metros quadrados eh {round(m,2)}")