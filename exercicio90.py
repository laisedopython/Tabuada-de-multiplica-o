#Dada a lista numeros = [10, 20, 30, 40, 50, 60, 70]:
# Calcule a soma de todos os elementos da lista usando um laço.
# Some apenas os três primeiros elementos da lista.
# Imprima os dois resultados.
lista_numeros = [10, 20, 30, 40, 50, 60, 70]
soma = 0
soma2 = 0
for i in lista_numeros:
    soma += i
lista_nova = lista_numeros[0:3]
for f in lista_nova:
    soma2 += f
print("A soma de todos os números é {}".format(soma))
print("A soma dos três primeiros numeros é {}".format(soma2))


