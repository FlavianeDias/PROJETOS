# pegar altura e largura da parede e calcular quanros litros de tinta vai utilizar sendo que cada 2m vai 1litro
larg=float(input('entre aqui com a largura da parede: '))
alt=float(input('entre aqui com a altura da parede: '))
area=larg*alt
tinta=area/2
print('A area da parede é de {}m²\nVoce vai precisar de {} Litros de tinta'.format(area,tinta))