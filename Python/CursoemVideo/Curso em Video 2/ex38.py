n1 = int(input('Digite aqui um valor: '))
n2 = int(input('Digite aqui um segundo valor: '))
if n1 > n2:
    print('O primeiro valor {} é maior que o segundo {}'.format(n1,n2))
elif n1 < n2:
    print('O segundo valor {} é maior que {}'.format(n2,n1))
else:
    print('Os valores são iguais')
