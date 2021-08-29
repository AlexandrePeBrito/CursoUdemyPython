#Escrevendo em arquivos -> Ao abrir um arquivo para leitura, não podemos realizar a escrita.
#Da mesma forma que se a gente abrir para escrita não poderá ler o arquivo

""" with open("CursoUdemyPython/Modulo6/novo.txt",'w') as arquivo:      #caso n tenha eh criado o arquivo
    arquivo.write("Ola mundo!\n")                               
    arquivo.write("Podemos escrever varias linhas")
    #arquivo.write(5)                                               #obrigatorio ser String
    arquivo.write("hahaha\n"*15)                                    #Escrever 15 vezes  """    


with open("CursoUdemyPython/Modulo6/novo.txt",'w') as arquivo:  
    while True:
        fruta=input("Informe uma fruta ou Digite Sair ")
        if(fruta!='sair'):
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break