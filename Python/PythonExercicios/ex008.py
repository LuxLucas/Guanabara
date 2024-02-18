print(f'{"METRO, CM E MM":=^50}')
while True:
    try:
        valorEmMetros = float(input("Digite o valor em metros:"))
        break
    except (ValueError, TypeError) as erro:
        print(f'{"CARACTERE INVÁLIDO":=^50}')
print(f'{"RESULTADO":=^50}')
print('Metros (M): {}'.format(valorEmMetros))
print('Centímetros (CM): {}'.format(valorEmMetros*100))
print('Milímetros (MM): {}'.format(valorEmMetros*1000))
print(f'{"FIM":=^50}')
