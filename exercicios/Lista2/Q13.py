#Faça um algoritmo que calcule a média ponderada das notas
#de 3 provas. A primeira e a segunda prova tem peso 1 e
#a terceira tem peso 2. Ao final, mostrar a média do aluno
#e indicar se o aluno foi aprovado ou reprovado. 
#A nota para aprovação deve ser igual ou superior a 60 pontos.
notas=[]
i=1
for c in range(0,3):
    if(i<3):
        n=float(input("Informe a nota do aluno de 0 ate 10: "))
        if(n>=0 and n<=10):
            n=n*1
            notas.append(n)
    elif(i==3):
        n=float(input("Informe a nota do aluno de 0 ate 40: "))
        if(n>=0 and n<=40):
            n=n*2
            notas.append(n)   
    i+=1

media=sum(notas)/3
if(media>=60):
    print("Aprovado")
elif(media<60):
    print("Reprovado")