nome = input("digite o nome do aluno(a): ")
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))

media = ((n1+n2+n3)/3)

print("a media do aluno(a): {} é: {:.2f} " .format(nome,media))