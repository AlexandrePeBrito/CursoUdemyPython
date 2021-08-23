# *args eh utilizado como parametro para n deixar fixo 
#exemplo

def soma(*args):
    print(args)

soma(1)
soma(1,2)
soma(1,2,4)

# **kwargs eh utilizado como parametro para n deixar fixo em formato de dicionario
#exemplo
def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"{pessoa} {cor}")
cores(a='azul',v='verde',f='branco',s='amarelo')