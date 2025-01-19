#Solicite ao usuário que digite uma frase. Conte quantas vogais (a, e, i, o, u) existem na frase e 
# exiba o resultado.
# Dica: Use o for para percorrer cada caractere da frase e verifique se é uma vogal.
frase_digitada = input("Digite uma frase: ")
vogais = 'AaEeIiOoUu'
contagem = 0
for i in frase_digitada:
    if i in vogais:
        contagem += 1
print(contagem)