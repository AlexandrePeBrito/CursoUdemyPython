""" 10. Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O
arquivo de entrada contém em cada linha o nome de uma cidade (ocupando 40 caracte-
res) e o seu número de habitantes. O programa deverá ler o arquivo de entrada e gerar
um arquivo de saída onde aparece o nome da cidade mais populosa seguida pelo seu
número de habitantes. """

arq1=input("Informe o caminho do arquivo de entrada: ")#'CursoUdemyPython/exercicios/Lista6/arq.txt'
arq2=input("Informe o caminho do arquivo de saida: ")#'CursoUdemyPython/exercicios/Lista6/saida.txt'
arquivo1=open(arq1)
arquivo2=open(arq2,'w')
linhas=arquivo1.readlines()  
cidade=[]
maior=0
for c in range(len(linhas)):
       cidade.append(linhas[c].split(','))
       if(int(cidade[c][1])>maior):
           maior=int(cidade[c][1])
for i in range(len(linhas)):
    if(int(cidade[i][1])==maior):
        arquivo2.write(cidade[i][0])
        arquivo2.write(cidade[i][1])
        break
print("finalizado")


