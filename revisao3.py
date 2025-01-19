#Dada a tupla numeros = (15, 22, 8, 14, 37, 42, 50, 31, 18):
# Filtre apenas os números pares em uma nova lista.
# Conte quantos números são maiores que 20.
# Desempacote os três primeiros números da tupla em variáveis.
# Imprima os resultados.
tupla_numeros = (15, 22, 8, 14, 37, 42, 50, 31, 18)
maiorque20 = 0
for i in tupla_numeros:
    if i % 2 == 0:
        print(i)
    if i >=  20:
        maiorque20 += 1
a, b, c = tupla_numeros[0:3]

print(maiorque20)
print(a, b, c)
