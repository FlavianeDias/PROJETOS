import random
from time import sleep
nuum = int(input('Tente adivinhar um numero aleatorio que estou pensando de  1 a 5: '))
print('Processando...')
sleep(3)
result = (random.randrange(1,5))
if nuum == result:
    print('Parabens você acertou! {}'.format(result))
else:
    print('Desculpe mas você errou! o certo é: {} '.format(result))
