""" 4. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
letras são vogais e quantas são consoantes.
 """
v=0
cons=0
arquivo=open('CursoUdemyPython/exercicios/Lista6/arq.txt')
texto=arquivo.read()
for c in texto:
    if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        v+=1
    else:
        cons+=1
arquivo.close()
print(f"Foi identificado um total de {v} vogais e {cons} consoantes,")

       
   
        
  
