NomeCidade = input('Sua cidade: ').strip().upper().split()

print(f'{"RESPOSTA":=^50}')

if NomeCidade[0] == 'SANTO':
    print('Começa com "SANTO"')
else:
    print('Não começa com "SANTO"')

