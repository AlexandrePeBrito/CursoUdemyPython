""" 
Criando sua propria versao de LOOP`
    for num in [1,2,4,5,6,8]:
        print(num)

    for letra in "alexandre":
        print(letra)
"""

def meu_for(interavel):
    it=iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('alexandre')