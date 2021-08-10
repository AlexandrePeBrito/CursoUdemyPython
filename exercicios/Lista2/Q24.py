#Uma empresa vende o mesmo produto para quatro diferentes 
#estados. Cada estado possui uma taxa diferente de imposto
#sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um 
#programa em que o usuário entre com o valor e o estado 
#destino do produto e o programa retorne o preço final do
#produto acrescido do imposto do estado em que ele será 
#vendido. Se o estado digitado não for válido, mostrar uma
#mensagem de erro.

prod=(float(input("Informe o valor do produto: ")))
estado=input("Informe seu estado(MG, SP, RJ, MS): ")

if(estado=='MG'):
    prod=prod*1.07
elif(estado=='SP'):
    prod=prod*1.12
elif(estado=='Rj'):
    prod=prod*1.15
elif(estado=='MS'):
    prod=prod*1.08

print(f"O valor do produto eh {prod}")
