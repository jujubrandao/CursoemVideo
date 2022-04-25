#R$60,00 por dia | R$0,15 por km rodado
p = float(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))
t = (p * 60) + (k * 0.15)

print('O total a pagar é R${}.'.format(t))
