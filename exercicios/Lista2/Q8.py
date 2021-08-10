#Faça um programa que leia 2 notas de um aluno, verifique
#se as notas são válidas e exiba na tela a média destas 
#notas. Uma nota válida deve ser, obrigatoriamente, um
#valor entre 0.0 e 10.0, onde caso a nota não possua 
#um valor válido, este fato deve ser informado ao 
#usuário e o programa termina.
notas=[]
i=0
for c in range(0,2):
    n=float(input("Informe a nota do aluno: "))
    if(n>=0 and n<=10):
        notas.append(n)
    else:
        print("valor invalido")
        break
