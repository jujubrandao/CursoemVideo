num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma = soma + num
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')

