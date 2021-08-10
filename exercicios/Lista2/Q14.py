#A nota final de um estudante é calculada a partir de 
#três notas atribuídas entre o intervalo de O até 10,
#respectivamente, a um trabalho de laboratório, a uma
#avaliação semestral e a um exame final. A média das
#três notas mencionadas anteriormente obedece aos pesos:
#Trabalho de Laboratório: 2; Avaliação Semestral: 3;
#Exame Final: 5. De acordo com o resultado, mostre na 
#tela se o aluno está reprovado (média entre 0 e 2,9),
#de recuperação (entre 3 e 4,9) ou se foi aprovado. 
#Faça todas as verificações necessárias.
notas=[]
i=1
for c in range(0,3):
    if(i==1):
        n=float(input("Informe a nota do aluno( de 0 a 3): "))
        if(n>=0 and n<=3):
            n=n*2
            notas.append(n)
        else:
            print("Nota invalida")
            i=0
            break
    if(i==2):
        n=float(input("Informe a nota do aluno( de 0 a 3): "))
        if(n>=0 and n<=3):
            n=n*3
            notas.append(n)
        else:
            print("Nota invalida")
            i=0
            break
    if(i==3):
        n=float(input("Informe a nota do aluno( de 0 a 3): "))
        if(n>=0 and n<=3):
            n=n*5
            notas.append(n)
        else:
            print("Nota invalida")
            i=0
            break

if(i!=0):
    media=sum(notas)/3
    if(media>4.9):
        print("Aluno Aprovado")
    elif(media<=4.9 and media >=3):
        print("Aluno em Recuperação")
    elif(media<3 and media>=0):
        print("Aluno Reprovado")