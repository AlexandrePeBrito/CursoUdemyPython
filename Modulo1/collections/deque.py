# Modulo Collection -> Deque

#Deque -> Lista de alta performance

from collections import deque

dek =deque('alexandre')

print(dek)

#Adicionando elementos


dek.append('y')
dek.appendleft('o')
print(dek)

dek.pop()
dek.popleft()
print(dek)
