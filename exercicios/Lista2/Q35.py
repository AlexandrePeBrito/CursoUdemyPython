#Leia uma data e determine se ela é válida. Ou seja, verifique
#se o mês está entre 1 e 12, e se o dia existe naquele mês.
#Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias
#em anos não bissextos.

dia=int(input("Informe um dia: "))
mes=int(input("Informe um mes(1 ate 12): "))
ano=int(input("Informe um ano: "))

if(ano<2022):
    if(1<=mes<=12):
        if(1<=dia<=31):
            if((mes==2) and ((ano%4==0 and ano%100!=0)or(ano%400==0))and(1<=dia<=28)):
                print("Data Valida")
            else:
                print("Data Valida")
        else:
            print("Data Invalida")
    else:
        print("Data Invalida")
else:
    print("Data Invalida")
