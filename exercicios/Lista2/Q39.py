#Uma empresa decide dar um aumento aos seus funcionários de 
#acordo com uma tabela que considera o salário atual e o 
#tempo de serviço de cada funcionário. Os funcionários com 
#menor salário terão um aumento proporcionalmente maior do
#que os funcionários com um salário maior, e conforme o 
#tempo de serviço na empresa, cada funcionário irá receber 
#um bônus adicional de salário. Faça um programa que leia:

#O valor do salário atual do funcionário;
#O tempo de serviço desse funcionário na empresa (número 
#de anos de trabalho na empresa).

#Use as tabelas abaixo para calcular o salário reajustado 
#deste funcionário e imprima o valor do salário final
#reajustado, ou uma mensagem caso o funcionário não tenha
#direito a nenhum aumento.

#Salário Atual        |Reajuste(%) | Tempo de Serviço  |   Bônus   |
#Até 500,00           |     25%    |  Abaixo de 1 ano  | S/ Bonus  |
#Até 1000,00 100,00   |     20%    |   De 1 a 3 anos   |    100    |
#Até 1500,00 200,00   |     15%    |   De 3 a 6 anos   |    200    |
#Até 2000,00          |     10%    |  De 7 a 10 anos   |    300    |
#Acima de 2000,00     | S/ Reajuste|  Mais de 10 anos  |    500    |

salario_antigo=float(input("Inform seu sarario: "))
temp_serv= int(input("Informe o tempo de trabalho na empresa: "))

if(salario_antigo<=500 and temp_serv<1):
    salario_novo=salario_antigo*1.25
elif(500<salario_antigo<=1000 and 1<temp_serv<=3):
    salario_novo=(salario_antigo*1.2)+100
elif(1000<salario_antigo<=1500 and 3<temp_serv<=6):
    salario_novo=(salario_antigo*1.15)+200
elif(1500<salario_antigo<=2000 and 7<temp_serv<=10):
    salario_novo=(salario_antigo*1.1)+300
elif(2000<salario_antigo and 10<temp_serv):
    salario_novo=salario_antigo+500

print(f"O salario atualizado do cliente eh {salario_novo}")