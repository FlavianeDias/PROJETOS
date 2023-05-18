#vista dinheiro/cheque 10% //a vista cart 5% de desconto // em 2x preço formal/3x ou mais no cartão: 20% de juros
print('==Loja==')
valor = float(input('Digite aqui o valor da compra: '))
print('OPÇÕES DE PAGAMENTO\n [1] A vista dinheiro/cheque\n [2] A vista no cartão\n'
      ' [3] 2x no cartão\n [4] 3x no cartão')
op = int(input('Digite a opção de pagamento: '))

if op == 1:
    valorf= (valor - (valor*0.10))
    print('O valor da compra será de: ', valorf)