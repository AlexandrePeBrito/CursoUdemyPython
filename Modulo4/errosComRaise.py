# raise -> lança as exceções
#Iremos criar nosso proprio erro nas funçoes
#Forma de utilizar:
#  raise tipoDeErro("Mensagem de erro")

#obs: Nao eh uma função, eh uma palavra reservada igual o "def"
#OBs: Dps do RAISE tudo eh ignorado

#exemplo
#raise ValueError("Valor incorreto")

#exemplo real

def colore(texto,cor):
    cores=['azul','verde','amarelo','vermelho']
    if (type(texto) is not str):
        raise TypeError("Texto precisa ser string")
    if (type(cor) is not str):
        raise TypeError("Cor precisa ser string")
    if (cor not in cores):
        raise ValueError(f"A cor Precisa estar entre {cores}")
    print(f"O texto {texto} sera impresso na cor {cor}")

colore('a',"verde")