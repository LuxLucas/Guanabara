Nome = input(f'Seu nome: ').upper()
Nome = Nome.split()

print(f'{"RESPOSTA":=^50}')

print(f'Primeiro Nome: {Nome[0]}')
print(f'Último Nome: {Nome[len(Nome)-1]}')
print(f'Abreviação: {Nome[0]+" "+Nome[len(Nome)-1]}')

