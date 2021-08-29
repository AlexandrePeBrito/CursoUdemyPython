#StringIO ->Utilizado para ler e escrever arquivos em memoria

#Para ler um arquivo do sistema operacional precisa de permissão, Permissao de leitura e escrita

#Para usar precisa fazer o import
from io import StringIO

mensagem='esta eh uma string'

arquivo=StringIO(mensagem)
print(arquivo.read())
arquivo.write("\tMais coisas")
arquivo.seek(0)
print(arquivo.read())
