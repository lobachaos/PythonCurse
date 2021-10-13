string = "O Brasil é penta"

lista = string.split(' ')
lista2 = string.split(',')

print(lista)
print(lista2)

for valor in lista:
    print(f'"{valor}", aparece {lista.count(valor)}x vezes na frase')

nova_string = '*'.join(lista)

print(nova_string)

# Enumerate gera tuplas
for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])
