#Uma empresa contrata um encanador a R$30,00 por dia.
#Faça um programa que solicite o número de dias trabalhados
#pelo encanador e imprima a quantia líquida que deverá ser
#paga, sabendo-se que são descontados 8% para imposto de renda.

num_dias=int(input("Informe o numeros de dias trabalhados: "))
salario=(30*num_dias)*0.92
print(f"O salario do encanador eh {salario}")