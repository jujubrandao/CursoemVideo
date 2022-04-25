casa = float(input('Valor da casa: '))
salário = float(input('Sálario do comprador: '))
anos = int(input('Quantos anos de financiamento? '))
# calcular prestação mensal
# descobrir prestação mensal | pm não pode exceder 30% do salário
# se comprador ganha 10.000, pm não pode exceder 3.000
# teria sido melhor escrever os nomes em vez de incógnitas, para visualizar nelhor a resolução do problema
prestação = casa / (anos * 12)
mínimo = salário * 30/100
if prestação <= mínimo:
    print(f'Para pagar uma casa de R${casa} em {anos} anos, a prestação será de R${prestação:.2f}.')
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print(f'Para pagar uma casa de R${casa} em {anos} anos a prestação será de R${prestação:.2f}.')
    print('Empréstimo NEGADO!')
