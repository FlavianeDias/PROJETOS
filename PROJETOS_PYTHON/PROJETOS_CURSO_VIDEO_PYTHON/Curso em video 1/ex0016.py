# crie um programa que leia um numero quebrado e print ele inteiro utilizando uma biblioteca math
from math import trunc
num = float(input('entre aqui com o seu numero'))
print('num é {}  o resultado em valor inteiro {}.'.format(num, trunc(num)))