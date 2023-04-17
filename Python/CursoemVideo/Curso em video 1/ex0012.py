#calculo de desconto apenas 5%
print('\nSe você comprar um produto e o valor for a vista no dinheiro o desconto é de 5% ')
valor = float(input('Entre aqui com o Valor total da compra: '))
novo = valor - (valor*5/100)
print('O Valor de {}  com 5% de desconto é de {}'.format(valor,novo))
