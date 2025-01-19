#Peça ao usuário para digitar uma palavra e exiba essa palavra invertida usando um laço for.
palavra_digitada = input("Digite uma palavra: ")
palavra_invertida = ' '    # não sei a palavra invertida, então coloco um espaço
for i in range((len(palavra_digitada) - 1), -1, -1):   #percorro a palavra de trás pra frente
    palavra_invertida += palavra_digitada[i]           #me refiro aos is sucessivos
print(palavra_invertida)
