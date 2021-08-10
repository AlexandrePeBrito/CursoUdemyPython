#Leia a nota e o número de faltas de um aluno, e escreva seu
#conceito. De acordo com a tabela abaixo, quando o aluno tem
#mais de 20 faltas ocorre uma redução de conceito.

#      Nota     |Conceito(ate 20)   |Conceito(mais de 20)
#   9 ate 10    |          A        |          B            |
#   7.5 ate 8.9 |          B        |          C            |
#   5 ate 7.4   |          C        |          D            |
#   4 ate 4.9   |          D        |          E            |
#   0 ate 3.9   |          E        |          E            |

n_faltas=int(input("Informe o numero de faltas: "))
nota=float(input("Informe o numero de faltas: "))

if(9<=nota<=10 and n_faltas>20):
    print("Sua nota conceito eh B")
elif(9<=nota<=10 and n_faltas<=20):
    print("Sua nota conceito eh A")
elif(7.5<=nota<=8.9 and n_faltas>20):
    print("Sua nota conceito eh C")
elif(7.5<=nota<=8.9 and n_faltas<=20):
    print("Sua nota conceito eh B")
elif(5<=nota<=7.4 and n_faltas>20):
    print("Sua nota conceito eh D")
elif(5<=nota<=7.4 and n_faltas<=20):
    print("Sua nota conceito eh C")
elif(4<=nota<=4.9 and n_faltas>20):
    print("Sua nota conceito eh D")
elif(4<=nota<=4.9 and n_faltas<=20):
    print("Sua nota conceito eh E")
elif(0<=nota<=3.9 and n_faltas>20):
    print("Sua nota conceito eh E")
elif(0<=nota<=3.9 and n_faltas<=20):
    print("Sua nota conceito eh E")

