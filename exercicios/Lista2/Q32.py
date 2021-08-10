#Escrever um programa que leia o código do produto escolhido 
#cardápio de uma lanchonete e a quantidade. O programa deve 
#calcular o valor a ser pago por aquele lanche.Considere que
#a cada execução somente será calculado um pedido. O cardápio
#da lanchonete segue o padrão abaixo:

#Especificação    | Codigo  | Preço |
#[Gachoro Quente  |   100   | 1.20  |
#[Bauru Símples   |   101   | 1.30  |
#[Bauru c/Ovo     |   102   | 1.50  |
#[Hamburguer      |   103   | 1.20  |
#[Cheeseburguer   |   104   | 1.70  |
#[suco            |   105   | 2.20  |
#[Retigerane      |   106   | 1.00  |

cardapio={100:1.2,101:1.3,102:1.5,103:1.2,104:1.7,105:2.2,106:1}

print(cardapio)
pedido=int(input("Informe o cod do pedido: "))
qnt=int(input("Informe a quantidade: "))

valor=cardapio[pedido]*qnt
print(f"O valor total eh {round(valor,1)}")

