#Leia a idade e o tempo de serviço de um trabalhador e escreva
#se ele pode ou não se aposentar. As condições para 
#aposentadoria são
#* Ter pelo menos 65 anos,
#*Ou ter trabalhado pelo menos 30 anos,
#*Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade=int("Informe a idade: ")
temp_serv=int("Informe o tempo de serviço: ")

if(idade>=65):
    print("Pode se aposentar")
elif(temp_serv>=30):
    print("Pode se aposentar")
elif(idade>=60 and temp_serv>=25):
    print("Pode se aposentar")
else:
    print("NAO pode se aposentar")