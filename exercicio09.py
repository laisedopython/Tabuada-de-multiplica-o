#Peça ao usuário um número inteiro positivo. 
# Use um laço para exibir uma pirâmide com os números até o número digitado.
numero_digitado = input("Digite um número inteiro positivo: ")
formando_a_palavra = ' '
for i in numero_digitado: #percorre a string
    formando_a_palavra += i
    print(formando_a_palavra)