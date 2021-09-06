""" 1. Escreva um programa que:
(a) Crie/abra um arquivo texto de nome “arq.txt”
(b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário
entre com o caractere '0'
(c) Feche o arquivo
Agora, abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracte-
res armazenados. """

arquivo=open('CursoUdemyPython/exercicios/Lista6/arq.txt','a')
texto=''
while(texto!='0'):
    texto=input('Informe a frase ou Digite 0 para sair: ')
    if(texto=='0'):
        arquivo.close()
    else:
        arquivo.write(texto)
        arquivo.write('\n')
arq=open('CursoUdemyPython/exercicios/Lista6/arq.txt')
print(arq.read())
arquivo.close()