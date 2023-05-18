nome = str(input('Digite seu nome completo: ')) .strip()
nome1 = nome.split()
print('Seu primeiro nome é: {} e seu ultimo nome é: {} '.format(nome1[0],nome1[-1]))