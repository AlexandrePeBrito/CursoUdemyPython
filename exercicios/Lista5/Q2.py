#2. Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela
#no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de
#2000.
def dataExtenso(data):
    data=data.split('/')
    dia=int(data[0])
    mes=int(data[1])
    ano=int(data[2])
    if(dia>0 and dia<32):
        if(0<mes and mes<13):
            if(ano<=2021):
                if(mes==1):
                    print(f"{dia} de Janeiro de {ano}")
                elif(mes==2):
                    print(f"{dia} de Fevereiro de {ano}")
                elif(mes==3):
                    print(f"{dia} de Março de {ano}") 
                elif(mes==4):
                    print(f"{dia} de Abril de{ano}")
                elif(mes==5):
                    print(f"{dia} de Maio de {ano}")
                elif(mes==6):
                    print(f"{dia} de Junho de {ano}")
                elif(mes==7):
                    print(f"{dia} de Julho de {ano}")
                elif(mes==8):
                    print(f"{dia} de Agosto de {ano}")
                elif(mes==9):
                    print(f"{dia} de Setembro de {ano}")
                elif(mes==10):
                    print(f"{dia} de Outubro de {ano}")
                elif(mes==11):
                    print(f"{dia} de Novembro de {ano}")
                elif(mes==12):
                    print(f"{dia} de Dezembro de {ano}")
            else:
                print("Data Invalida!")
        else:
            print("Data Invalida!") 
    else:
        print("Data Invalida!")
dt=input("Informe umda data no formato DD/MM/AAAA: ")
dataExtenso(dt)