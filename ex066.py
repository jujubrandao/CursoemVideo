'''num = soma = 0
while num != 999:
    num = int(input('Digite um valor [999 para parar]: '))
    soma += num
    print(f'A soma dos valores foi {soma}')
print('Acabou!')'''
soma = cont = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    soma += num


