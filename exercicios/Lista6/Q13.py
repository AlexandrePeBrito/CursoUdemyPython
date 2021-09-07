""" 13. Faça um programa que permita que o usuário entre com diversos nomes e telefone para
cadastro, e crie um arquivo com essas informações, uma por linha. O usuário finaliza a
entrada com '0' para o telefone.
 """
verify='a'

with open("CursoUdemyPython/exercicios/Lista6/questao13.txt",'w') as arquivo:  
    while True:
        if(verify!='0'):
            nome=input("Informe o nome: ")
            telefone=input("Informe o telefone: ")
            arquivo.write(f'{nome} {telefone}')
            arquivo.write('\n')
            verify=input("Para sair digite 0 ")
        else:
            break
        