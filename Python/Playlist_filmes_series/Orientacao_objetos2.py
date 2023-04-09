class Filmes:
    def __int__(self, nome, ano, duracao):
    self.nome = nome
    self.ano = ano
    self.duracao = duracao

vingadores = Filmes('Vingadores - Guerra infinita', 2018, 160)
print(vingadores.nome)