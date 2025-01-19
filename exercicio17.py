#Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], faça o seguinte:
# Obtenha e imprima os três primeiros elementos da lista.
# Obtenha e imprima os três últimos elementos da lista.
# Obtenha e imprima todos os elementos, exceto os dois primeiros.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[0:3])
print(lista[-1:-4:-1])
dois_primeiros = lista[0:2]
print(dois_primeiros)
lista_nova = lista - dois_primeiros
print(lista_nova)
