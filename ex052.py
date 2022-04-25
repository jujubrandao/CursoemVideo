num = int(input('Digite um número: '))
tot = 0
for contador in range (1, num + 1):
    if num % contador == 0:
            print('\033[33m', end=" ")
            tot += 1
    else:
            print('\033[31m', end=" ")
    print(f'{contador}', end=" ")
print(f'\n\033[mO número {num} foi divisível {tot} vezes. ')
if tot == 2:
    print('E por isso, ele é primo.')
else:
    print('Desse modo, ele não é primo.')

