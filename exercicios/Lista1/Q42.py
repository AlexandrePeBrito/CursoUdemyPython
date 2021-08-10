#Recebao salário-base de um funcionário. 
#Calcule e imprima o salário a receber, sabendo-se 
#que esse funcionário tem uma gratificação de 5% 
#sobre o salário-base. Além disso, ele paga 7% de 
#imposto sobre o salário-base.

salario_base=float(input("Informe o salario do funcionario: "))

salario_final=salario_base*1.05
salario_final=salario_final*0.93

print(f"O salario final do funcionario eh {salario_final}")