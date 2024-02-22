print(f'{"AUMENTO DE SALÁRIO EM 15%":=^50}')
while True:
    try:
        salario = float(input('Qual o seu salário (R$)?: '))
        break
    except ValueError as erro:
        print(f'\n{"CARACTERE INVÁLIDO":=^50}')
print(f'\n{"NOVO SALÁRIO":=^50}')
print('Parabéns, seu novo salário será de R$ {:.2f}'.format(salario + (salario * 0.15)))
