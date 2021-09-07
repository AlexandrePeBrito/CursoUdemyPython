""" 
Geradores ->
    - geradores sao iterators(iteradores)
    obs: mas nem todos iterators sao geradores
geradores podem ser criados por funções geradoras
funções geradoras utilizam palavra reservada yield
geradores podem ser criados por Expressoes Geradoras


Diferença de Função e Funções geradoras
--------------------------
funções
    utilizam return
    retorna uma vez
    quando executada, retorna um valor

funções geradoras
    utilizam yield
    podem utilizar o yields multiplas vezes
    quando executada, retorna um gerador
"""

#exemplo de funçao geradores
def conta_ate(valor_max):
    c=1
    while c <= valor_max:
        yield c
        c+=1
#obs: função geradores n sao geradores mas criam geradores
gen=conta_ate(5)
print(type(gen))
print(next(gen))
print(next(gen))
