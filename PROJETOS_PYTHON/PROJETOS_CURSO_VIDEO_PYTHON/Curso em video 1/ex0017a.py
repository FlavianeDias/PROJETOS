#resolução mais simples do exercicio da hipotenusa
from math import hypot
a= float(input('digite aqui o adjacente '))
b = float(input('digite aqui o oposto'))
h= hypot(a,b)
print('o hipotenusa é {}'.format(h))