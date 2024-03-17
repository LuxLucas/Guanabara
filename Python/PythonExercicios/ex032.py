# Importando módulo datetime
from datetime import date

# Recebe o ano
Ano = int(input('Digite um ano (0: ano atual): '))

# Informa o ano atual
if Ano == 0:
    Ano = date.today().year

# Confirma se o ano é bissexto (366 dias):
if (Ano % 4 == 0) and (not (Ano % 100 == 0) or (Ano % 400 == 0)):
    Resultado = True
else:
    Resultado = False

print(f'{"RESULTADO":=^50}')

# Traduz o resultado
if Resultado:
    print(F'O ano {Ano} É BISSEXTO')
else:
    print(F'O ano {Ano} NÃO É BISSEXTO')
