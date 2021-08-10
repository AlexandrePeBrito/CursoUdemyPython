#Leia o salário de um trabalhador e o valor da prestação
#de um empréstimo. Se a prestação for maior que 20% 
#do salário imprima: Empréstimo não concedido, caso 
#contrário imprima: Enpréstimo concedido.

salario=float(input("Informe o salario do trabalhador: "))
emprestimo=float(input("Informe o valor do emprestimo: "))

status=emprestimo/salario
if(status>0.2):
    print("Emprestimos não consedido")
elif(status<=0.2):
     print("Emprestimos consedido")