p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))

if p > s:
    print(f'O primeiro número é MAIOR')
elif p < s:
    print(f'O segundo número é MAIOR')
else:
    print(f'Os números são IGUAIS')

#try e except do curso do coursera, para não vir a
#mensagem de erro, quando, por exemplo, se inserir
#uma letra onde é pedido um número
#palavras úteis: try, except, quit