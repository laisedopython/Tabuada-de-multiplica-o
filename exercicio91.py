#Dada a tupla dados = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
# Obtenha uma nova tupla contendo apenas os 5 primeiros elementos de dados.
# Desempacote os valores dessa nova tupla em variáveis individuais.
# Imprima cada número da tupla original usando um laço
tupla_original = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
nova_tupla = tupla_original[0:5]
print("Os 5 primeiros números são {}".format(nova_tupla))
for i in nova_tupla:
    print(i)
for f in tupla_original:
    print(f)
