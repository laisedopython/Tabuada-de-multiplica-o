#Peça ao usuário para digitar a quantidade de números da sequência de Fibonacci que ele 
# deseja ver e exiba esses números.
# Solicita ao usuário a quantidade de números da sequência de Fibonacci
quantidade = int(input("Quantos números da sequência de Fibonacci você quer ver? "))

# Inicializa os dois primeiros números da sequência
anterior, atual = 0, 1

print("Sequência de Fibonacci:")

# Gera e exibe a sequência de Fibonacci
for _ in range(quantidade):
    print(anterior, end=" ")
    anterior, atual = atual, anterior + atual
