#Dado na lista alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]:
# Obtenha todos os elementos, mas pulando 2 de cada vez.
# Obtenha os elementos das posições 2 a 8, pulando 3 de cada vez.
# Inverta os elementos da lista com um passo de -2.
# Obtenha os últimos 5 elementos na ordem inversa.
# Obtenha os 3 primeiros elementos seguidos pelos 3 últimos, usando fatiamento
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
print(lista[0::2])
print(lista[1::2])
print(lista[2:9:3])
print(lista[::-2])
print(lista[-1:-6:-1])
lista_a = lista[:3]
lista_b = lista[-3:]
lista_a.extend(lista_b)
print(lista_a)