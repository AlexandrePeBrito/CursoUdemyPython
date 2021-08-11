#Faça um algoritmo que converta uma velocidade expressa em 
#km/h para m/s e vice versa. Você deve criar um menu com as
#duas opções de conversão e com uma opção para finalizar o
#programa. O usuário poderá fazer quantas conversões desejar,
#sendo que o programa só será finalizado quando a opção de
#finalizar for escolhida.

menu=int(input("1-Converter KM/h em M/s\n2-Converter \
M/s em KM/h\n3-Sair:\t"))
while(menu!=3):
    if(menu==1):
        km=float(input("Informe o KM/h: "))
        ms=km/3.6
        print(f"\n{km} km/h corresponde a {round(ms,1)} M/s\n")
        menu=int(input("1-Converter KM/h em M/s\n2-\
Converter M/s em KM/h\n3-Sair:\t"))
    elif(menu==2):
        ms=float(input("Informe o KM/h: "))
        km=ms*3.6
        print(f"\n{round(ms,1)} M/s corresponde a {km} km/h\n")
        menu=int(input("1-Converter KM/h em M/s\n2-\
Converter M/s em KM/h\n3-Sair:\t"))
    else:
        print("\nOpção invalida!\n")
        menu=int(input("1-Converter KM/h em M/s\n2-\
Converter M/s em KM/h\n3-Sair:\t"))
