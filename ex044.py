print('=========== Lojas Guanabara ============')
preço = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTOS: ')
print(' [ 1 ]: à vista com dinheiro ou cheque')
print(' [ 2 ]: à vista no cartão')
print(' [ 3 ]: 2x no cartão')
print(' [ 4 ]: 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    npreço = preço - (10/100 * preço)
    print('Você está compando à vista e receberá 10% de desconto.')
    print(f'Sua compra de {preço} irá custar {npreço} agora')
elif opção == 2:
    npreço2 = preço -(5/100 * preço)
    print('Bom, você está comprando à vista no cartão. Receberá 5% de desconto.')
    print(f'Sua compra no valor de {preço} irá custar agora {npreço2}')
elif opção == 3:
    print('Ok. Em até duas vezes no cartão, você paga o preço normal. Sem descontos, sem juros, pequeno gafanhoto.')
    print(f'Assim, seu valor final de custo será o mesmo de compra, ou seja, {preço}')
elif opção == 4:
    npreço3 = preço + (20/100 * preço)
    print('Em mais de 3x não conseguimos manter o preço. Será aplicado 20% de juros. Que pena.')
    print(f'Sua compra no valor de {preço} passará a ser {npreço3}')
else:
    print('Ih, não temos essa opção aqui na loja.\nTenta outra, gafanhote.')

