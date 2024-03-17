NomePessoa = input('Sua nome: ').strip().upper().split()

print(f'{"RESPOSTA":=^50}')

if 'SILVA' in NomePessoa:
    print('Possui "SILVA"')
else:
    print('Não possui "SILVA"')

