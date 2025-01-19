# Solicita ao usuário um número inteiro positivo
numero_inteiro = input("Digite um número inteiro positivo: ")

# Inicializa a variável para armazenar a soma dos dígitos
soma = 0

# Percorre cada caractere (dígito) na string do número
for letra in numero_inteiro:
    # Converte o caractere para inteiro e adiciona à soma
    soma += int(letra)

# Exibe o resultado
print(f"A soma dos dígitos de {numero_inteiro} é: {soma}")
