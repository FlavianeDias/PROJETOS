#fazer uma lista aleatoria com os alunos
from random import shuffle
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite aqui o nome do segundo aluno: '))
c = str(input('Digite aqui o nome do terceiro aluno: '))
d = str(input('Digite aqui o nome do quarto aluno: '))
lista = [a,b,c,d]
shuffle(lista)
print('A ordem seleciona é {}'.format(lista))