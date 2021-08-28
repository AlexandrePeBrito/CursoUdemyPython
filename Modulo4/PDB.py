#Debugando usand o PDB

#PDB -> Python Debugger

#Debugar codigo usando print eh ruim
""" def dividir(a,b):
    print(f"a={a} b={b}")
    try:
        return int(a)/int(b)
    except (ValueError,ZeroDivisionError) as err:           
        print(f"Ocorreu um erro! {err}")         
    
print(dividir(4,7)) """

#Existem formas profissionais de usar o Debugger

def dividir(a,b):
    try:
        return int(a)/int(b)
    except (ValueError,ZeroDivisionError) as err:           
        print(f"Ocorreu um erro! {err}")         
    
print(dividir(4,7)) 