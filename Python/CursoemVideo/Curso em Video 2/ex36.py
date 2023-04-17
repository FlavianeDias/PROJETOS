#emprestimo
valor = float(input('Digite aqui o valor do imovel: '))
an = int(input('Digite aqui em quantos anos deseja pagar: '))
salario = float(input('Digite aqui o valor do seu salario: '))
prestacao = (valor/an)/12 
if prestacao <= (salario*0.3):
    print('O seu empretimo esta aprovado!!! ')
elif prestacao > (salario*0.3):
    print('No momento não podemos aprovar o seu emprestimo!')