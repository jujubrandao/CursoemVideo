p = float(input('Qual é o salário do funcionário? R$'))
k = (p + 0.10 * p)
h = (p + 0.15 * p)
if p > 1250:
    print(f'Quem ganhava {p} passa a ganhar {k:.2f} agora')
if p < 1250:
    print(f'Quem ganhava {p} passa a ganhar {h:.2f}')
