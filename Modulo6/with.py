#Bloco WITH eh utilizada para criar contexto de trabalho



with open("CursoUdemyPython/Modulo6/test.txt") as arquivo:    #nao precisa fechar, so funciona no with
    print(arquivo.readlines())
