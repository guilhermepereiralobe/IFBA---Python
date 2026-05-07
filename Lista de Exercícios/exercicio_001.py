# Proposta: dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu perímetro.

# A = b X h
# A é a área, b é a base e h é a altura.

def calcular_ratangulo(bd, hd):
    if bd >= 1 and hd >= 1:
        a = bd * hd
        print(f'A área de um retângulo com a base {bd}cm e altura de {hd}cm é igual a {a}cm²')
    else:
        print("Faça de novo.")

# Repetição.
while True:
    b = float(input('[cm] Valor da base: '))
    h = float(input('[cm] Valor da altura: '))
    print(calcular_ratangulo(bd=b, hd=h))
    
# Função.
# Validação do número.
# Tratamento de erro.
