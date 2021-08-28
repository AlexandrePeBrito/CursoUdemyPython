#usamos Try/Except para tratar erros que possam ocorrer no codigo. Previnindo que o programa
# pare de funcionar

#OBS:tratar erro de forma generica não eh a melhor forma de tratar o erro de forma especifica

#Forma de utilizar:
#try:
#   codigo
#Except:
#   O que deve ser feito caso tenha algum problema

#Exemplo de forma Generica 1
#try:
#    funcao()        #função nao inicializada
#except:
    #print("Deu erro")

#Exemplo de forma Generica 2
#try:
#    len(1)        #função Len não funciona com inteiros
#except:
    #print("Deu erro 2")


#Exemplo de forma Especifica 1
#try:
#    funcao()        #função nao inicializada
#except NameError:
#    print("Função Inexistente")

#Exemplo de forma Especifica 1
#try:
#    len(1)        #função nao inicializada
#except TypeError:
#    print("Função com Parametros errado")

#Tratando diversos erros
#try:
    #len(1)
    #funcao()
#    print('lista'[8])
#except TypeError:
#    print("Erro do tipo TypeError")
#except NameError:
#    print("Error do tipo NameError")
#except:
#    print("Error diferente")

#Exemplo REAL
def pega_valor(dicionario,chave):
    try:
        return dicionario[chave]
    except:
        return None

dic={'1':'alexandre'}
print(pega_valor(dic,'4'))