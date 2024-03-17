# Recebe salario do funcionário
Salario = float(input('Seu salário: '))

# Declaração do aumento em porcentagem
Aumento = [0.10, 0.15]

# Calcula bônus salarial
if Salario > 1250:
    Bonus = Salario * Aumento[0]
else:
    Bonus = Salario * Aumento[1]

# Calcula novo salário
NovoSalario = Salario + Bonus

print(f'{"RESULTADO":=^50}')

# Imprimi resultado
print(f'Seu salário atual é de R$ {NovoSalario:,.2f}')
