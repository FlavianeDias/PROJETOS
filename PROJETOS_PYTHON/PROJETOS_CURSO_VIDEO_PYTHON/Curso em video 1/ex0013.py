#ler valor do salario e calcular aumento de 15%
salario = float(input('Entre aqui com o valor do salario do empregado: '))
novo = salario +(salario*15/100)
print('O salario é de {:.2f} o novo valor que o empregado deverá receber com 15% de aumento é de {:.2f}'.format(salario,novo))
