print(f'{"PRODUTO COM 5% DE DESCONTO":=^50}')
while True:
    try:
        valorProduto = float(input('Qual o preço (R$) de seu produto ?: '))
        break
    except ValueError as erro:
        print(f'\n{"CARACTERE INVÁLIDO":=^50}')
print(f'\n{"PREÇO COM DESCONTO":=^50}')
print('O novo preço é de R$ {:.2f}'.format(valorProduto - (valorProduto * 0.05)))              
