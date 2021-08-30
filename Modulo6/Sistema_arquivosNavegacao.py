#Sistemas de arquivos e manipulação

# Para fazer uso da manipulção de arquivos do sistema operacional precisamos
#importar e fazer uso do modulo OS
#Operating System

import os
""" 
print(os.getcwd())  #Mostrar qual direitorio esta rodando este documento #  D:\Meus Documentos\Documentos\GitHub

os.chdir('..')      #muda o direitorio deste documento,
print(os.getcwd())     # D:\Meus Documentos\Documentos
os.chdir('..')      
print(os.getcwd())     # D:\Meus Documentos
os.chdir('..')      
print(os.getcwd())     # D:\

print(os.path.isabs('D:\Meus Documentos\Documentos'))       #Retorna boolean se o direitorio eh absoluto



print(os.getcwd())                              #D:\Meus Documentos\Documentos\GitHub
resp= os.path.join(os.getcwd(),'teste','teste1')     #Entrando na pasta teste 
os.chdir(resp)                                  #fazendo mudança
print(os.getcwd())                              #D:\Meus Documentos\Documentos\GitHub\teste\teste1
 
print(os.listdir())             #Gera uma lista com os arquivos
print(os.listdir('D:\\'))       #Gera uma lista com os arquivos da raiz
"""

#Usando Listdir()
arquivo=os.listdir()
print(arquivo)
print(arquivo[0])

#Usando scandir()-> Usado para ter mais detalhes dos direitorios
arquivo1=list(os.scandir()) 
print(arquivo1)
print(dir(arquivo[0]))                  #DIR mostra oq tem na função desejada

