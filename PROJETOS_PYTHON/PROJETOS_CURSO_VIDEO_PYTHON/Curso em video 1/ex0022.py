#mexendpo com strings e manipulando
nome = str(input('Digite aqui seu nome completo: ')).strip()
print('Seu nome em letra MAIUSCULA É: ', nome.upper())
print('Seu nome em letras MINUSCULAS É: ', nome.lower())
print('Seu nome no total tem {} caracter'.format(len(nome) - nome.count(' ')))
pnome = nome.split()
print('O primeitro nome é {} e tem {} caracter'.format(pnome[0], len(pnome[0])))
