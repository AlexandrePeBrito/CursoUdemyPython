#Faça um programa que calcule e mostre a soma dos 50 
#primeiros números pares.

c=1
u=0
while(c!=0):
    if(c%2==0):
        print(c)
        u+=1
    if(u==30):
        break
    c+=1
print(u)
