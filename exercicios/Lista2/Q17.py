#Faça um programa que calcule e mostre a área de um trapézio.
#Sabe-se que: #A=((basemaior + basemenor) + altura)/2

#Lembre-se a base maior e a base menor devem ser números maiores que zero.

base_menor=float(input("Informe o tamanho da base menor: "))
base_maior=float(input("Informe o tamanho da base maior: "))
altura=float(input("Informe o tamanho da altura: "))

area=((base_maior+base_menor)*altura)/2

print(f"Area do trapezio eh {area}")