#Leia um valor de complimento em centimentros e apresente-o convertido em polegadas.
#A formula de conversao eh: P=C/2.54,
#sendo C o comprimento em centimetros e P o comprimento em polegadas

cent=int(input("Informe o comprimento em centimetros: "))

p=cent/2.54

print(f"O comprimento em polegadas eh {round(p,2)}")