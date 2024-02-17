import string
nome = input('Qual é mesmo seu nome ? \n')
nome = string.capwords(nome)
print('Olá, Mundo. Este é '+nome+'. \nOlá, '+nome+'. Este é Mundo.')
