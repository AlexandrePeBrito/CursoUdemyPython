"""  Iterator -> 
        *Um objeto que pode ser iterado
        *Um objeto que retorna um dado um elemento por vez
       
    Iteraveis->
        *Um objeto q ira retornar um iterator quando a função iter() for chamada
        Exemplo = Strings, Listas
        nome='alexandre'    
        lista=[2,4,6,5,7]

    OBS:iterator retorna um dado e um iterable retorna um iterator
"""


nome='alexandre' 
#print(next(nome)) #error

it=iter(nome)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
