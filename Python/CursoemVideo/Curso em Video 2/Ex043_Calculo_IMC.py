#Classificação IMC < 18,5: Abaixo do Peso/18,5 e 25: Peso Ideal/ 25 até 30: Sobrepeso
# 30 até 40: Obesidade/ > 40: Obesidade Mórbida
peso = float(input('Digite aqui seu peso em kg: '))
altura = float(input('Digite aqui a sua altura: '))
imc = (peso / (altura*altura))
print('{:.2f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso!!!')
elif imc > 18.5 and imc <= 25:
    print('Voce esta no peso ideal!!')
elif imc >25 and imc <=30:
    print('Voce esta sobrepeso!!!')
elif imc > 30 and imc <=40:
    print('Voce esta com obesidade!!!')
else:
    print('Voce esta com obesidade Morbida!!!')