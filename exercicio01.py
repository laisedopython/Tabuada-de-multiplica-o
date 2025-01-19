#Peça ao usuário para digitar um número, e use um laço for para exibir a tabuada desse número de 1 a 10.
numero_digitado = int(input("Digite um número: "))
for i in range(1, 11):
    print(f'{numero_digitado} x {i} = {numero_digitado * i}')
    