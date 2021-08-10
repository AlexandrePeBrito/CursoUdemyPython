#Escreva um programa de ajuda para vendedores. 
#A partir de um valor total lido,
#mostre: e o total a pagar com desconto de 10%;
#o valor de cada parcela, no parcelamento de 3x sem juros;
#a comissão do vendedor, no caso da venda ser 
#a vista (5% sobre o valor com desconto) a comissão 
# do vendedor, no caso da venda ser parcelada 
#(5% sobre o valor total)

valor_total=float(input("Informe o valor total: "))
opcao=int(input("1-Parcelada\n2-A vista "))

valor_desconto=valor_total*0.9
parcela=valor_total/3
comissao_vista=valor_desconto*0.05
comissao_parcelada=valor_total*0.05

if(opcao==1):
    print(f"Valor total = {valor_total}\n\
Valor da parcela = {parcela}\n\
Comissão = {comissao_parcelada}")
elif(opcao==2):
    print(f"Valor total = {valor_desconto}\n\
Comissão = {comissao_vista}")