print(f'{"PINTANDO A PAREDE":=^50}')
largura = ''
altura = ''
while True:
    try:
        largura = float(input('Qual a largura de sua parede em metros ?: '))
        altura  = float(input('Qual a altura de sua parede em metros ?: '))
        break
    except ValueError as erro:
        print(f'\n{"CARACTERE INVÁLIDO":=^50}')

print(f'\n{"RESULTADO":=^50}')
area = altura * largura
areaTinta = area / 2
print('Área da parede em metros: {}m²'.format(area))
print('Tinta nescessária para pintá-la: {:.2f}L\n'.format(areaTinta))
