#radar eletronico
vel = float(input('Digite aqui a velocidade artual do carro: '))
if vel <= 80.00:
    print('Tenha um bom dia! Dirija com cuidado.')
else:
    mult = ((vel-80)*7)
    print('MULTADO, acima do limeite permitido \n Multa de R$ ', mult)