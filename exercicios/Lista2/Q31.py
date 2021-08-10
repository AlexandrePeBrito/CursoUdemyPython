#Faça um programa que receba a altura e o peso de uma pessoa. 
#De acordo com a tabela a seguir, verifique e mostra qual a 
#classificação dessa pessoa.

#Altura          |ate 60 |60-90 |acima de 90
#Menor que 1,20 | A     | D    | G 
#De 1,20 a 1,70 | B     | E    | H 
#Maior que 1,70 | C     | F    | I 

peso=float(input("Informe o peso: "))
altura=float(input("Informe a altura: "))

if(altura<1.2 and peso<60):
    print("Classificação A")
elif((altura<1.2) and (60<peso<90)):
    print("Classificação D")
elif((altura<1.2) and (60<peso<90)):
    print("Classificação G")
elif(1.2<altura<1.7 and peso<60):
    print("Classificação B")
elif(1.2<altura<1.7 and (60<peso<90)):
    print("Classificação E")
elif(1.2<altura<1.7 and (60<peso<90)):
    print("Classificação H")
elif(altura>1.7 and peso<60):
    print("Classificação C")
elif(altura>1.7 and (60<peso<90)):
    print("Classificação F")
elif(altura>1.7 and (60<peso<90)):
    print("Classificação I")
