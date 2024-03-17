from math import trunc
print(f'\n{"PARTE INTEIRA DE UM NÚMERO":=^50}')
while True:
    try:
        numeroRecebido = float(input('Digite um número: '))
        break
    except ValueError as erro:
        print(f'\n{"CARACTERE INVÁLIDO":=^50}')
print(f'\n{"RESULTADO":=^50}')
print('Número digitado: {}\nParte inteira: {}'.format(numeroRecebido, trunc(numeroRecebido)))