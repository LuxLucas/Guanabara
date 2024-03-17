Cores= {
    "Limpa": '\033[m',
    "Vermelho": '\033[31m',
    "Azul": '\033[34m',
    "Branco": '\033[1;4;7;40m'
}

print(f'Olá, {Cores["Azul"]}Lucas{Cores["Limpa"]}. '
      f'Está gostando de {Cores["Branco"]} trocar as cores {Cores["Limpa"]} ?')
