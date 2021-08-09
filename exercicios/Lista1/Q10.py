#Leia uma velocidade em km/h e apresente-a convertida em m/s.
#Formula da conversao eh : M=K/3.6    ;
#Sendo K a velocidade em KM e M em M/s

k=float(input("Informe A velocidade em KM/h: "))

M=k/3.6
print(f"A velocidade convertida eh {round(M,1)} M/s")