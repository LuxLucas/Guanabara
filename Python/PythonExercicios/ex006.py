print(f'{"DOBRO, TRIPLO E RAÍZ":=^50}')
while True:
    numeroDigitado = input('Digite um número:')
    if numeroDigitado.isnumeric():
        numeroDigitado = float(numeroDigitado)
        break
    else:
        print(f'\n{"NÚMERO digitado é INVÁLIDO":=^50}')
print("Seu dobro: {}".format(numeroDigitado*2))
print("Seu triplo: {}".format(numeroDigitado*3))
print("Sua raís quadrada: {}".format(numeroDigitado**(1/2)))
print(f'{"FIM":=^50}')
