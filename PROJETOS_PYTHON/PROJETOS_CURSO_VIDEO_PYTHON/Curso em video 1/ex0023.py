#ler um numero de 0 a 999 (precisei ver o video)
num = int(input('Digite aqui um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
d = num // 1000 % 10
print('unidade: {}'.format(u))
print('Dezena: ', d)
print('Centena: ', c)
print('Milhar: ', d)