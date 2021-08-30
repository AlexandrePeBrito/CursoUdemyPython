# Sistema de Arquivos - Manipulação
import os
#Descobrindo se um direitorio ou arquivo existe
""" print(os.path.exists('CursoUdemyPython'))
print(os.path.exists('test.txt'))                   #Não existe na pasta GitHub, esta dentro da aba do curso udemy
print(os.path.exists('CursoUdemyPython\\Modulo6\\test.txt'))        #acessando para verificar

#criando arquivo
#forma1 ->menos convencionais
open('arquivoteste.txt','w').close()        #Criou no direitorio GitHub
#forma2->menos convencionais
open('arquivoteste.txt','a').close()        #Criou no direitorio GitHub
#forma3->menos convencionais
with open('arquivoteste.txt','a') as arquivo:        #Criou no direitorio GitHub
    pass

#Criando Direitorio
#OBS: Caso não tenha permissao gera um PermissionError
os.mkdir("tesao")                               #Caso ja exista tera um erro FileExistsError
os.mkdir('CursoUdemyPython\\Modulo6\\tes')      #Caso ja exista tera um erro FileExistsError


os.makedirs('CursoUdemyP\\Modulo7\\tes', exist_ok=True)        #Cria conjunto de direitorios, caso ja existe ele ignora
 
#Renomeando arquivos
os.rename('CursoUdemyP','CursoUdemyPy')

os.rename('CursoUdemyPy\\Modulo7','CursoUdemyPy\\modulo')       #precisa colocar o caminho


#Deleta arquivos   ->Deleta apenas arquivos
#Obs: o arquivo deletado não vai para lixeira, ele some
os.remove('teste.txt')              #caso nao exista da erro

#Deleta Direitorios
os.rmdir("aleatorio")               #Caso o direitorio tenha algo dentro não eh deletado

#Removendo uma Arvore do direitorio
os.removedirs('CursoUdemyPy\\modulo')
os.removedirs('CursoUdemyPy')
"""




