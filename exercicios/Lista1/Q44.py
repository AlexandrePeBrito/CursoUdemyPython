#Receba a altura do degrau de uma escada e 
#a altura que o usuário deseja alcançar subindo a escada. 
#Calcule e mostre quantos degraus o usuário deverá 
#subir para atingir seu objetivo.

altura_degrau=float(input("Informe a altura do degrau: "))
altura=int(input("Informe o andar que deseja chegar: "))

qnt_degraus=altura/altura_degrau

print(f"O numeros de degraus para subir ate o ponto desejado eh {qnt_degraus}")