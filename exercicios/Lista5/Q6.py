#6. Faça uma função que receba 3 números inteiros como parâmetro, representando horas,
#minutos e segundos, e os converta em segundos.
def convertSeg(horas,min,seg):
    horaSeg=(horas*60)*60
    minSeg=min*60
    return horaSeg+minSeg+seg

h=int(input("Informe as horas: "))
m=int(input("Informe os minutos: "))
s=int(input("Informe os segundos: "))
segundos=convertSeg(h,m,s)
print(f"O total de segundos eh {segundos}")