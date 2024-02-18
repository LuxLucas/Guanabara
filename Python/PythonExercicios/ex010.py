# Conversão considerada por Gustavo Guanabara:
# R$ 3,27 = U$ 1,00
print(f'{"CONVERSÃO PARA DÓLAR":=^50}')
while True:
    try:
        dinheiroAtual = float(input('Quanto dinheiro você tem (R$):'))
        break
    except (TypeError, ValueError) as erro:
        print(f'{"CARACTERE INVÁLIDO":=^50}')
print(f'\n{"RESULTADO":=^50}')
print('Você possui (R$): {}'.format(dinheiroAtual))
print('Você pode comprar (U$): {:.2f}'.format(dinheiroAtual/3.27))
print(f'{"FIM":=^50}')
