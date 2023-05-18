# crie um codigo que faça o valor da hipotenusa de forma simples utilizando uma biblioteca
#eu que fiz
from math import pow
from math import
a = int(input('Digite aqui o cateto adjacente: '))
b = int(input('Digite aqui o cateto oposto: '))
h = sqrt((pow(a,2))+(pow(b,2)))
print('o calculo dos catetos {} e {} tem como hipotenusa {}'.format(a,b,h))