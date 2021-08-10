#Leia um valor de complimento em polegadas e apresente-o convertido em centimetros.
#A formula de conversao eh: C=P*2.54,
#sendo C o comprimento em centimetros e P o comprimento em polegadas


polegadas=int(input("Informe o comprimento em polegadas: "))

c=polegadas*2.54

print(f"O comprimento em centimetro eh {round(c,2)}")