#Modos de leitura de arquivos

#'r'    ->Abre para leitura
#'w'    ->Abre para escrita
#'x'    ->Abre para escrita se o arquivo não existir
#'a'    ->Abre para escrita adicionando no final do arquivo caso ja exista
#'+'    ->Abre arquivo para leitura e escrita

""" with open("CursoUdemyPython/Modulo6/test.txt",'x') as arquivo:  #ERROR pois existe o .txt
    arquivo.write('ola') """

""" with open("CursoUdemyPython/Modulo6/test2.txt",'x') as arquivo:  #Correto
    arquivo.write('ola') """

""" with open("CursoUdemyPython/Modulo6/test.txt",'a') as arquivo:  #Adicionou no final do arquivo
    arquivo.write('\ncaralho') """

with open("CursoUdemyPython/Modulo6/test.txt",'r+') as arquivo:  
    arquivo.write('\ncaralho') 