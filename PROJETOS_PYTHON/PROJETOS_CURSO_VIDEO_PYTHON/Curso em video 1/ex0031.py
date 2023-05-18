#preço viagem
distc = float(input('digite aqui a distancia da viagem: '))
if distc<=200.00:
    print('O preço da viagem vai ser de R${:.2f}'.format(distc*0.5))
else:
    print('O preço da viagem vai ser de R${:.2f}'.format(distc*0.45))