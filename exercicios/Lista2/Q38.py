#Leia uma data de nascimento de uma pessoa fornecida 
#através de três números inteiros:
#Dia, Mês e Ano. Teste a validade desta data para saber se
#esta é uma data válida. Teste se o dia fornecido é um dia
#válido: dia > O, dia < 28 para o mês de fevereiro (29 se o
#ano for bissexto), dia < 30 em abril, junho, setembro e 
#novembro, dia < 31 nos outros nmeses. Teste a validade do
#mês: mês > O e mês < 13. Teste a validade do ano: ano <
#ano atual (use uma constante definida com o valor igual 
#a 2008). Imprimir: “data válida” ou “data inválida” no 
#final da execução do programa.

dia=int(input("Informe o dia do seu aniversario(Em numeros): "))
mes=int(input("Informe o mes do seu aniversario(Em numeros): "))
ano=int(input("Informe o ano do seu aniversario(Em numeros): "))

if(ano<2022):
    if(1<=mes<=12):
        if(1<=dia<=31):
            if((mes==2) and ((ano%4==0 and ano%100!=0)or(ano%400==0))and(1<=dia<=28)):
                print("Data Valida")
            elif(mes==2 and (1<=dia<=28)):
                print("Data Valida")
            elif(mes!=2 and (1<=dia<=31)):
                print("Data Valida")
            else:
                print("Data Invalidaalida")
        else:
            print("Data Invalida")
    else:
        print("Data Invalida")
else:
    print("Data Invalida")