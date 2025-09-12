# dias do carro alugado 60 reais e 0,15 por kilometros rodados
dias= int(input('Entre aqui quantos dias o carro ficou em uso: '))
kl = float(input('Entre aqui com quantos kilometros foi rodado: '))
alu = 60*dias+(kl*0.15)
print('O aluguel do carro ficou em {:.2f} reais'.format(alu))