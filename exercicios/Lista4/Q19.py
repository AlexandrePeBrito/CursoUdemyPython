#Faça um vetor de tamanho 50 preenchido com o seguinte valor:
#(i +5*1)%(i+1), sendo i a posição do elemento no vetor. 
#Em seguida imprima o vetor na tela.
vetor=[]
for c in range(0,50):
    vetor.append((c+5*1)%(c+1))
print(vetor)