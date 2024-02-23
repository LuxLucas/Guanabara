print(f'{"CONVERTENDO TEMPERATURA: C PARA F E K":=^50}')
while True:
    try:
        temperaturaCelsius = float(input('Declare uma temperatura em °C: '))
        break
    except ValueError as erro:
        print(f'\n{"CARACTERE INVÁLIDO":=^50}')
print(f'\n{"RESULTADO DA CONVERSÃO":=^50}')
temperaturaKelvin = temperaturaCelsius - 273
temperaturaFahrenheit = ((temperaturaCelsius * 9) + 160)/5
print('\nTemperatura em °C: {}\nTemperatura em °F: {}\nTemperatura para K: {}'.format(temperaturaCelsius, temperaturaFahrenheit, temperaturaKelvin))

