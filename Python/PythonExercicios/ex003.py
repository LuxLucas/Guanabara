print('*****SOMANDO*****')
while True:
    try:
        primeiroNumero = input('Digite seu primeiro número:')
        segundoNumero = input('Digite seu segundo número:')

        if primeiroNumero.isnumeric() and segundoNumero.isnumeric():
            primeiroNumero = float(primeiroNumero)
            segundoNumero = float(segundoNumero)
            somaDeNumeros = primeiroNumero + segundoNumero
            break
        else:
            print('\nCaractere digitado é INVÁLIDO, repita.\n')
    except ValueError as erro:
        print('Tipo de erro:', erro, '\n')
print('O resultado da SOMA entre {} e {} é {}'.format(primeiroNumero, segundoNumero, somaDeNumeros))
print('*****FIM*****')
