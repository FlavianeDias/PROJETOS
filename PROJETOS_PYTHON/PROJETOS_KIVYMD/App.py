# codigo que vai rodar de fundo sem interface
print('CALCULE SEUS APORTES SEGUNDO O LIVRO SEGREDOS DE UMA MENTE MILIONARIA')
salario = int(input('Digite aqui o seu salario: '))
print('Segundo o livro você teria que dividir seu salario em: ')
invest = salario * 0.2
dcd = salario * 0.1
contas = salario * 0.5
print('50% Contas: {:.2f} \n20% Investimentos: {:.2f} \n10% Diversão: {:.2f}\n10% Conhecimento: {:.2f} \n10% Doação:{:.2f}'.format(contas,invest,dcd,dcd,dcd))