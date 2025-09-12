class Filmes:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Series:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filmes('Vingadores', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}')

atlanta = Series('Atlanta', 2017,2)
print('Nome: {} \nAno: {} \nTemporadas: {}'.format(atlanta.nome,atlanta.ano,atlanta.temporadas))