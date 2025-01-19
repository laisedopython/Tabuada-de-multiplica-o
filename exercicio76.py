palavra_contada = 'perfume'
palavra_digitada = input("Digite uma palavra: ")
while len(palavra_digitada) != 1:
    palavra_digitada = input("Digite uma palavra: ")
if palavra_digitada in palavra_contada:
    print()
