#Escreva um programa que leia um número inteiro maior do 
#que zero e devolva, na tela, a soma de todos os seus 
#algarismos. Por exemplo, ao número 251 corresponderá 
#o valor (2+5+1). Se o número lido não for maior do 
#que zero, o programa terminará com a mensagem 
#“Número inválido”.

num=int(input("Informe um numero inteiro: "))
txt_compl=[]
if(num>0):
    algoritmo=str(num)
    txt=f"{algoritmo[0]} "
    txt_compl.append(txt)
    for c in range(1,len(algoritmo)):
        txt=f"+ {algoritmo[c]} "
        txt_compl.append(txt)
    print(f"O valor {num} corresponde a {txt_compl}")