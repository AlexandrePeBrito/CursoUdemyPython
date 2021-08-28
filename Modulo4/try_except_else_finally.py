#Try/Except/Else/Finally

#DICA DE QUANDO E ONDE TRATAR O CODIGO -> Toda entrada de dados deve ser tratada

#Else e finally não eh muito comum
#Else -> Executa caso não ocorra o erro

#Usando o else
""" try:
    num=int(input("Informe um numero: "))        #Verifica se digitou um valor correspondete ao type 
except ValueError:
    print("Voce digitou um valor invalido")      #caso seja não passe ira para mensagem de erro
else:
    print(f"Voce digitou {num}")                 #Se passar executa """

#Finally -> Sempre sera executado independente do que ocorrer. Geralmente para 
# fechar ou desalocar recursos
#Usando o Finally
""" try:
    num=int(input("Informe um numero: "))        #Verifica se digitou um valor correspondete ao type 
except ValueError:
    print("Voce digitou um valor invalido")      #caso seja não passe ira para mensagem de erro
else:
    print(f"Voce digitou {num}")                 #Se passar executa
finally:
    print("Executando finally") """

#Exemplo complexo -> Errado
""" def dividir(a,b):
    return a/b
try:
    n1=int(input("Informe um numero: "))
    n2=int(input("Informe um numero: "))
except ValueError:
    print("Eh necessario que seja um numero")
try:
    print(dividir(n1,n2))
except NameError:
    print("Valor incorreto") """

#Exemplo complexo -> Certo

""" def dividir(a,b):
    try:
        return int(a)/int(b)
    except ValueError:
        print("Valor incorreto")
    except ZeroDivisionError:
        print("Não eh possivel dividir um numero por 0")

n1=input("Informe um numero: ")
n2=input("Informe um numero: ")
print(dividir(n1,n2)) """

#Exemplo generico -> certo
""" def dividir(a,b):
    try:
        return int(a)/int(b)
    except:
        print("Ocorreu um erro")
   
n1=input("Informe um numero: ")
n2=input("Informe um numero: ")
print(dividir(n1,n2)) """

#Exemplo SEMI-generico -> certo
def dividir(a,b):
    try:
        return int(a)/int(b)
    except (ValueError,ZeroDivisionError) as err:           #coloco o erro em uma variavel
        print(f"Ocorreu um erro! {err}")                    #apresento o erro
   
n1=input("Informe um numero: ")
n2=input("Informe um numero: ")
print(dividir(n1,n2))