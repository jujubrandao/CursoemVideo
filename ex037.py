num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
esc = input('Sua opção: ')
binário = '1'
octal = '2'
hexadecimal = '3'

if esc == binário:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2::]}')

elif esc == octal:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2::]}')

else:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2::]}')

