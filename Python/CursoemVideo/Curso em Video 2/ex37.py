nuum = int(input('Digite o numero que deseja converter: '))
print('Escolha uma destas opções para converter o numero escolhido\n 1- binario \n 2- octal \n 3-hexadecimal')
escolha = int(input('Digite a opção desejada: '))
if escolha == 1:
    print('A conversão do numero {} para binario é {}'.format(nuum,bin(nuum)[2:]))
elif escolha ==2:
    print('O numero {} em octa é {}'.format(nuum,oct(nuum)[2:]))
elif escolha ==3:
    print('O numero {} em hexadecimal é {}'.format(nuum,hex(nuum)[2:]))
else:
    print('A opção não foi selecionada corretamente! ')
