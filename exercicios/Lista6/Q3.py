""" 3. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
letras são vogais.
 """
a,e,i,o,u =0,0,0,0,0
arquivo=open('CursoUdemyPython/exercicios/Lista6/arq.txt')
texto=arquivo.read()
for c in texto:
    if(c == 'a'):
        a+=1
    elif(c == 'e'):
        e+=1
    elif(c == 'i'):
        i+=1
    elif(c == 'o'):
        o+=1
    elif(c == 'u'):
        u+=1
arquivo.close()
print(f"Foi identificado um total de {a+e+i+o+u} vogais sendo {a} A, {e} E, {i} I, {o} O, {u} U,")