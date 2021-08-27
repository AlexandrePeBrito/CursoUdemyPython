# lambdas sao funções sem nome, ou seja, anonimas

#Exemplo de expressao em python
#def funcao(x):
#    return x*5
#print(funcao(3))
#print(funcao(5))


#Exemplo de expressao lambda
#calculo = lambda x: x*5

#print(calculo(3))
#print(calculo(5))


#expressao lambda com diversas variaveis
nome_completo = lambda nome,sobrenome: nome.strip().title()+ ' '+sobrenome.strip().title()
print(nome_completo('alexandre','brito'))

#OBS: Lambda pode ter 0 ate N entradas