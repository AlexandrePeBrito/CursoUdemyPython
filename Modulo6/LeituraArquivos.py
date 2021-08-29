# Para ler um arquivo usamos o open()

#Forma mais simples de usar o open() nos passamos apenas um parametro de entrada
# esta função retorna um __TextIOWrapper e eh com eles que trabalhamos

#OBS:para utilizar o open() o arquivo de leitura deve existir

#aarquivo = open("test.txt")                                     #Errado
arquivo = open("CursoUdemyPython/Modulo6/test.txt")#ESTA DESGRAÇA FUNCIONOU, Colocar o caminho percorrido 

print(arquivo.read())           #ler o arquivo
print(arquivo.read())           #Nao ira ler pois o cursor esta vazio
arquivo.close()