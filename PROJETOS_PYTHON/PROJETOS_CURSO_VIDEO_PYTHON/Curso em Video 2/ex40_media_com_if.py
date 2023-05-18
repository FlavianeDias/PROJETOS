# exercicio da media de dois alunos <5 reprovado // => 5 e 6.9 recuperação // => 7 aprovado
n1 = float(input('Digite aqui a primeira nota: '))
n2 = float(input('Digite aqui a segunda nota: '))
media = ((n1 + n2)/2)

if media < 5:
    print('Aluno(a) obteve {} de nota e foi REPROVADO!'.format(media))

elif 7 > media >=5:
    print('Aluno(a) obteve {} de nota e esta de RECUPERAÇÃO!'.format(media))

else:
    print('O aluno obteve {} de nota e esta APROVADO!'.format(media))
