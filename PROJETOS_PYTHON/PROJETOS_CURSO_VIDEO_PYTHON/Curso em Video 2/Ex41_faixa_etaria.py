#classificação de uma faixa etária Mirim/Infantil/Junior/Senior/Master
from datetime import date
nasc = int(input('Digite aqui o ano do seu nascimento: '))
ano_atual = (date.today().year)
idade = ((date.today().year) - nasc)

if idade <=9:
    print('O atleta tem {} anos\nClassificação: Mirim'.format(idade))
elif idade >9 and idade <=14:
    print('O atleta tem {} anos\nClassificação: Infantil'.format(idade))
elif idade >14 and idade <=19:
    print('O atleta tem {} anos\nClassificação: Junior'.format(idade))
elif idade >19 and idade <=25:
    print('O atleta tem {} anos\nClassificação: Senior'.format(idade))
else:
    print('O atleta tem {} anos\nClassificação: Master'.format(idade))