#Dadas as listas nomes = ["Alice", "Bob", "Carol", "Daniel"] e idades = [25, 30, 22, 28]:
# Combine as duas listas em uma lista de tuplas.
# Exiba o nome e a idade de cada pessoa.
# Mostre os dados na ordem inversa
# Listas iniciais
nomes = ["Alice", "Bob", "Carol", "Daniel"]
idades = [25, 30, 22, 28]

# Combine as duas listas em uma lista de tuplas
pessoas = list(zip(nomes, idades))

# Exiba o nome e a idade de cada pessoa
print("Nome e idade de cada pessoa:")
for nome, idade in pessoas:
    print(f"Nome: {nome}, Idade: {idade}")

# Mostre os dados na ordem inversa
pessoas_invertida = pessoas[::-1]

print("\nDados na ordem inversa:")
for nome, idade in pessoas_invertida:
    print(f"Nome: {nome}, Idade: {idade}")

