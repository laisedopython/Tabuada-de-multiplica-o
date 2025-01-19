#Calcular o fatorial de um número
numero_digitado = int(input("Digite um número: "))
fatorial = 1
for i in range(numero_digitado, 0, -1):
    print(i)
    fatorial = fatorial * i
print(fatorial)