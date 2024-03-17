Nome = input('Digite seu nome: ').strip()

NomeUpper = Nome.upper()
NomeLower = Nome.lower()
TamanhoNome = len(Nome.replace(' ',''))

NomeDividido = Nome.split()
TamanhoPrimeiroNome = len(NomeDividido[0])

print(f'{"RESULTADO":=^50}')

print(f'Nome Upper: {NomeUpper}')
print(f'Nome Lower: {NomeLower}')
print(f'Tamanho do nome sem espaço: {TamanhoNome}')
print(f'Tamanho do primeiro nome: {TamanhoPrimeiroNome}')

print(f'{"":=^50}', end='\n')
