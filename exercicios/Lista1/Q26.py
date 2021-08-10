#Leia um valor de area em metros quadrados e apresente-o convertido em hectares.
#a formula de conversao eh: H=M*0.0001
#sendo M a area em metros quadrado e H area em hectaries

m=float(input("Informe a area de metros quadrados: "))

h=m*0.0001

print(f"A area convertida em hectares eh {round(h,2)}")