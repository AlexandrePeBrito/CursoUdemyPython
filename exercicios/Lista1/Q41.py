#Faça um programa que leia o valor da hora de trabalho 
# (em reais) e número de horas trabalhadas no mês.
#Imprima o valor a ser pago ao funcionário, 
# adicionando 10% sobre o valor calculado.

valor_hr=float(input("Informe o valor da hora trabalhada: "))
hr_trab=int(input("Informe as horas trabalhadas: "))

salario=(valor_hr*hr_trab)*1.1

print(f"O salario do funcionario eh {salario}")

