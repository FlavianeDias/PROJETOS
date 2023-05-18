#crie um programa que calcule seno cosseno e tangente
import math
a = int(input('Digite aqui o angulo desejado: '))
b = math.radians(a)
print('O seno desejado é {:.2f} \n O cosseno {:.2f} \n E a tangente {:.2f}'.format(math.sin(b), math.cos(b), math.tan(b)))