#pegando a data atual e a data de nascimento p/ checagem da data de alistamento
from datetime import date
nasc = int(input('Digite aqui o ano do seu nascimento: '))
ano_atual = (date.today().year)
idade = ((date.today().year) - nasc)
if idade < 18:
    Qfalta = (18 - idade)
    Afalta = (ano_atual + Qfalta)
    print('Ainda falta {} anos para seu alistamento que será com 18 anos!!'.format(Qfalta))
    print('Seu alistamento será em {}!'.format(Afalta))
elif idade > 18:
    Jpassou = (idade - 18)
    Apassou = (ano_atual - Jpassou)
    print('Seu alistamento já passou {} anos!!'.format(Jpassou))
    print('Você devia ter se alistado no ano de {}!'.format(Apassou))

elif idade == 18:
    print('Seu alistamento será este ano {}!!'.format(date.today().year))
