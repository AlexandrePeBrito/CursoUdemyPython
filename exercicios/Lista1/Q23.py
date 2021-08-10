#leia um valor de comprimento em metros e apresente-o convertido em jardas.
#A formula de conversao eh: j=m/0.91,
#Sendo J o comprimento em jardas e M o comprimento em metros.

m=float(input("Informe o comprimento em metros: "))

j=m/0.91

print(f"O comprimento convertido em jardas eh {round(j,2)}")