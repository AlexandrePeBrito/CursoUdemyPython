#Escreva um programa completo que permita a qualquer aluno 
#introduzir, pelo teclado, uma sequência arbitrária de notas
#(válidas no intervalo de 10 a 20) e que mostre na tela,
#como resultado, a correspondente média aritmética. O número
#de notas com que o aluno pretenda efetuar o cálculo não será
#fornecido ao programa, o qual terminará quando for 
#introduzido um valor que não seja válido como nota de
#aprovação.
resp=1
valores=[]
i=0
while(resp==1):
    n=int(input("Informe uma nota: "))
    if(10<=n<=20):
        i+=1
        valores.append(n)
        print(n)
    resp=int(input("Deseja inserir mais numeros?1-SIM ou 2-NAO "))
    
media=sum(valores)/i
print(f"A media das suas notas eh {media}")