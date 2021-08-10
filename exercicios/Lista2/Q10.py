#Faça um programa que receba a altura e o sexo de uma 
#pessoa e calcule e mostre seu peso ideal, utiizando
#as seguintes fórmulas (onde /h corresponde à altura):
#* Homens: (72.7+h) — 58
#* Mulheres: (62,1+h) — 44,7

altura=float(input("Informe a altura do paciente: "))
genero=input("Informe o sexo do paciente: M - Masculino F - Feminino ")

if(genero=='M' or genero=='m'):
    peso_ideal=(72.7+altura)-58
elif(genero=='F' or genero=='f'):
    peso_ideal=(62.1+altura)-44.7

print(f"O peso ideal do paciente eh {peso_ideal}")