#Dada a lista numeros = [5, 10, 15, 20], realize as seguintes operações:
# Use pop para remover e armazenar o último número da lista em uma variável chamada ultimo_numero.
# Use append para adicionar o valor de ultimo_numero duas vezes à lista.
# Insira o número 12 na posição 2 usando insert.
# Remova o número da posição 1 usando del.
# Imprima a lista final.
lista = [5, 10, 15, 20]
ultimo_numero = lista.pop()
print(lista)
lista.append(ultimo_numero)
lista.append(ultimo_numero)
print(lista)
lista.insert(1, 12)
print(lista)
del lista[0]
print(lista)