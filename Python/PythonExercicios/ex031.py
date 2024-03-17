# Recebe a distância da viagem
Distancia = float(input('Distância da viagem (Km): '))

# Inverte valor negativo
if Distancia < 0:
    Distancia *= -1

# Calcula valor da passagem
if Distancia <= 200:
    Passagem = Distancia * 0.5
else:
    Passagem = Distancia * 0.45

print(f'{"RESULTADO":=^50}')

# Mostra resultado
print(f'Preço da passagem é de R$ {Passagem:.2f}')
