#O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão
#do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo
#de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao
#consumidor.

#CUSTO DE FÁBRICA               |% DO DISTRIBUIDOR | % DOS IMPOSTOS
#até R$512.000,00               |         5        |   isento
#entre R$12.000,00 e 25.000,00  |         10       |    15
#acima de R$25.000,00           |         15       |    20


custo_fabrica=float(input("Informe o custo de fabrica para construir um carro: "))

if(custo_fabrica>25000):
    custo_final=custo_fabrica+(custo_fabrica*1.15)+(custo_fabrica*1.2)
elif(12000<=custo_fabrica<=25000):
    custo_final=custo_fabrica+(custo_fabrica*1.1)+(custo_fabrica*1.15)
elif(custo_fabrica<12000):
    custo_final=custo_fabrica+(custo_fabrica*1.05)

print(f"O custo final do carro eh {custo_final}")