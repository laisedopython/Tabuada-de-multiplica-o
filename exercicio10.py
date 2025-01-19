#Solicite ao usuário dois números inteiros que definem um intervalo [inicio, fim]. 
# Exiba todos os números desse intervalo que são divisíveis por 3 e 5.
# Dica: Use o operador de módulo % dentro do laço para verificar divisibilidade.
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
for i in range(primeiro_numero, segundo_numero + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
