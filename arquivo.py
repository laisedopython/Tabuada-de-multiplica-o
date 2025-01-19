palavra_secreta = "kaladin"
letra_digitada = input("Digite uma letra: ")
contagem = 1
for letra_digitada in palavra_secreta:
    print(letra_digitada)
else:
    print('*')
    letra_digitada = input("Digite uma letra: ")
    contagem += 1
print("Você acertou com {} tentativas".format(contagem))

