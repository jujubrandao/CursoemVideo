d = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(d.count('A')))
print('A primeira letra A apareceu na posição {}'.format(d.find('A')+1))
print('A última letra A apareceu na posição {}'.format(d.rfind('A')+1))