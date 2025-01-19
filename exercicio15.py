#Dada a lista animais = ["gato", "cachorro"], faça o seguinte:
# Crie outra lista chamada novos_animais contendo "papagaio", "tartaruga".
# Use o método extend para adicionar os elementos de novos_animais à lista animais.
# Imprima a lista resultante.
primeira_lista = ['gato', 'cachorro']
segunda_lista = ['papagaio', 'tartaruga']
primeira_lista.extend(segunda_lista)
print(primeira_lista)