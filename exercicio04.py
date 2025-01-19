#Peça ao usuário para digitar uma palavra e conte quantas vogais há nessa palavra. 
# Use um laço for para verificar cada letra.
palavra_digitada = input("Digite uma palavra: ")
vogais = 'AaEeIiOoUu'
contador = 0
for letra in palavra_digitada:
    if letra in vogais:
        contador += 1
print("A quantidade de vogais na palavra {} é {}".format(palavra_digitada, contador))
