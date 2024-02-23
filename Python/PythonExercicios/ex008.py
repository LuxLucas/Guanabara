print(f'{"CONVERSOR DE DISTÂNCIA":=^50}')
while True:
    try:
        valorEmMetros = float(input("Digite o valor em metros:"))
        break
    except (ValueError, TypeError) as erro:
        print(f'{"CARACTERE INVÁLIDO":=^50}')
print(f'{"RESULTADO":=^50}')
print('A medida de {} corresponde a:'.format(valorEmMetros))
print(valorEmMetros/1000, 'Km')
print(valorEmMetros/100, 'Hm')
print(valorEmMetros/10, 'Dam')
print(valorEmMetros, 'm')
print(valorEmMetros*10, 'dm')
print(valorEmMetros*100, 'cm')
print(valorEmMetros*1000, 'mm')
print(f'{"FIM":=^50}')
