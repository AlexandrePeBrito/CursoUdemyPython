#Faça um programa para ler as dimensões de um 
#terreno (comprimento c e largura 1) bem como 
#o preço do metro de tela p. Imprima o custo 
#para cercar este mesmo terreno com tela.

c=float(input("Informe a comprimento do terreno: "))
l=float(input("Informe a largura do terreno: "))
p=float(input("Informe o preço do metro: "))

area=l*c
valor=area*p

print(f"O valor da pintura eh {valor}")