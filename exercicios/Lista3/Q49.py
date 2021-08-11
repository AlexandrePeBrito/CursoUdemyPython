#O funcionário chamado Carlos tem um colega chamado 
#João que recebe um salário que equivale a um terço 
#do seu salário. Carlos gosta de fazer aplicações na
#caderneta de poupança e vai aplicar seu salário 
#integralmente nela, pois está rendendo 2% ao mês. 
#João aplicará seu salário integralmente no fundo de
#renda fixa, que está rendendo 5% ao mês. Construa um 
#programa que deverá calcular e mostrar a quantidade de
#meses necessários para que o valor pertencente a João
#iguale ou ultrapasse o valor pertencente a Carlos. Teste
#com outros valores para as taxas.

salario_carlos=1000
salario_joao=salario_carlos/3
c=0
while(salario_carlos>salario_joao):
    c+=1
    salario_joao=salario_joao*1.05
    salario_carlos=salario_carlos*1.02
print(f"Em {c} o salario do Joao {round(salario_joao,0)} vai ser\
maior que o salario do Carlos {round(salario_carlos,0)}")
