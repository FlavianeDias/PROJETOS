#verificar se no nome tem silva
nome = str(input('Digite aqui o seu nome completo: ')) .strip() .lower()
print('Seu nome contem o sobrenome silva? true or false: {}'.format('silva' in nome))