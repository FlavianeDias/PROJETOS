ano = int(input('Digite aqui o ano que deseja consultar se é bissexto: '))
if (ano%4 == 0) and (ano%100 == 0) and (ano%400 == 0):
    print('Este é um ano bissexto!')
else: print('Este não é um ano bissexto!')