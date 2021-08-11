#Chico tem 1.50 metro e cresce 2 centímetros por ano, 
#enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano.
#Escreva um programa que calcule e imprima quantos anos
#serão necessários para que Zé seja maior que Chico.
altura_chico=1.5
altura_ze=1.1
c=0
while(altura_ze<=altura_chico):
    c+=1
    altura_chico=altura_chico+0.02
    altura_ze=altura_ze+0.03
altura_chico=altura_chico+0.02
altura_ze=altura_ze+0.03
print(f"Levou {c+1} anos para Ze ultrapassar chico.\
A altura de Ze eh {round(altura_ze,2)} e a altura de Chico\
 eh {round(altura_chico,2)}")