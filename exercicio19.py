#Dada a string frase = "Python é incrível", envie comandos para:
# Obter a palavra "Python".
# Obter a palavra "incrível".
# Obtenha apenas as letras "P", "y", "t", "h" da string.
# Reverter toda a frase.
# Obtenha os caracteres nas posições pares da string.
frase = "Python é incrível"
frase_repartida = frase.split()  #dividindo a frase em pedaços
print(frase_repartida)
print(frase_repartida[2])   #imprimindo a segunda palavra da lists
python = frase_repartida[0]  #pegando a primeira palavra da lista
print(python[0:4])  #imprimindo as 4 primeiras letras
print(frase[::-1])
print(frase[2::2])