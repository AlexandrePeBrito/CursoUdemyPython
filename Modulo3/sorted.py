# Nao confundir Sorted() com sort(). Sort() so funciona com listas. Sorted() funciona
# com qualquer iteravel

# OBS: No sorted() retorna uma lista e deixa o iteravel original intacto

lista=[8,9,4,2,7,6,1,3,8,5,4,9]
tupla=(8,9,4,2,7,6,1,3,8,5,4,9)

print(lista)
lista.sort()
print(lista)
print(tupla)
#tupla.sort()            #error


print(sorted(tupla))            #ordenando tuplas

nomes= ('alexandre','maiure','ana','carlos','joselito')
print(sorted(nomes))
