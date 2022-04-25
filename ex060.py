from math import factorial
núm = int(input('Digite um número para ver o seu fatorial: '))
f = factorial(núm)
print(f' O fatorial de {núm} é {f}.')

#Solução 2
'''
f = 1 (porque o fator mínimo de multiplicação para um número fatorial é 1)
núm = int(input('Digite um número para ver o seu fatorial: '))
print(f'Calculando {núm}!: ')
cont = n (ou seja, o contador começa com o valor de n)
while cont > 0:
    print(f'{cont} ,end=" ")
    print(' x ' if cont > 1 else ' = ',end=" ")
    f = f * cont (ou f *= cont | leia-se: fatorial recebe o fatorial vezes o cont)
    c -= 1 (leia-se: c recebe c menos 1)
    
print(f' O fatorial de {núm} é {f}.')





'''





