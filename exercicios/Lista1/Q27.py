#Leia um valor de area em hectares e apresente-o convertido em metros quadrados.
#a formula de conversao eh: M=H*10000
#sendo M a area em metros quadrado e H area em hectaries

h=float(input("Informe a area em hectares: "))

m=h*10000

print(f"A area convertida em metros quadrados eh {round(m,2)}")