#Escreva um programa que, dada a idade de um nadador, 
#classifique-o em uma das seguintes categorias:

#Infantil A | 5 a 7
#Infantil B | 8 a 10
#Juvenil A  | 11 a 13
#Juvenil B  | 14 a 17
#Sênior     | maiores de 18 anos

idade=int(input("Informe a idade: "))

if(5<=idade<=7):
    print("A sua categoria eh Infantil A")
elif(8<=idade<=10):
    print("A sua categoria eh Infantil B")
elif(11<=idade<=13):
    print("A sua categoria eh Juvanil A")
elif(14<=idade<=17):
    print("A sua categoria eh Juvanil A")
elif(18<=idade):
    print("A sua categoria eh Senior")