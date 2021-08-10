#Leia a distância em Km e a quantidade de litros de gasolina 
#consumidos por um carro em um percurso, calcule o consumo
#em K m/ e escreva uma mensagem de acordo com a tabela abaixo:

#CONSUMO    | (Km/l)  |  MENSAGEM
#menor que  |   8     | - Venda o carro
#entre      |[8 e 14] | - Econômico!
#maior que  |   12    | - Super economico!

distancia=int(input("Informe a distancia em KM: "))
gas=int(input("Informe a quantidade de gasolina em litros: "))

cons=distancia/gas

if(cons<8):
    print("Venda o Carro")
elif(cons>14):
    print("Super economico")
elif(8<=cons<=14):
    print("Econômico")