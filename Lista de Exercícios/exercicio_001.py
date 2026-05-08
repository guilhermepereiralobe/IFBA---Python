# Proposta: dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu perímetro.

# A = b X h
# A é a área, b é a base e h é a altura.

try:
    b = float(input('O valor da base: '))
    h = float(input('O valor da altura: '))
    a = b * h

    print(f'A área de um retângulo com a base de {b} cm e a altura de {h} cm é {a}')
except :
    print('Digite a base ou altura apenas com números e, o calculo já é em cm, ou seja, não precisa colocar ele.')
    print()
# Repetição.
# Função.
# Validação do número.
# Tratamento de erro.
