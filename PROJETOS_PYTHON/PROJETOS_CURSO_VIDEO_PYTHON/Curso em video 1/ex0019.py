# sorteio de um aluno
from random import choice
a = str(input('Digite aqui o primeiro aluno: '))
b = str(input('Digite aqui o segundo aluno: '))
c = str(input('Digite aqui o terceiro aluno: '))
d = str(input('Digite aqui o quarto aluno: '))
lista = [a,b,c,d]
print('O aluno escolhido foi : {}'.format(choice(lista)))