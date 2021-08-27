#all() Retorna TRUE se todos os elementos sao verdadeiros ou se estiver vazio

#exemplo
#print(all([1,5,3,4,8])) #verifica todos o elementos
#print(all([])) #verifica todos o elementos
#print(all([0,1,5,3,4,8])) #verifica todos o elementos
#print(all((1,5,3,4,8))) #verifica todos o elementos
#print(all((0,1,5,3,4,8))) #verifica todos o elementos
#print(all({1,5,3,4,8})) #verifica todos o elementos
#print(all({0,1,5,3,4,8})) #verifica todos o elementos
#nome=['alexandre','ana','amanda']
#print(all([n[0] == 'a' for n in nome])) 


#any() retorna true se qualquer elemento do iteravel for verdadeiro.

print(any([0,0,0,0,0,0,0,0]))
print(any([0,0,0,0,0,0,0,0,1]))
print(any([]))
print(any({0,0,0,0,0,0,0,0,1}))
print(any({0,0,0,0,0,0,0,0}))
print(any((0,0,0,0,0,0,0,0,1)))
print(any((0,0,0,0,0,0,0,0)))