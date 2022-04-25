print('-' *25)
print('Sequência de Fibonacci')
print('-' *25)
termos = int(input('Quantos termos você quer mostrar? ' ))
#fib--> o termo n é igual a soma dos dois termos anteriores (n=8 -> (5+3)
t1 = 0
t2 = 1
print('~'*25)
print(f'{t1}-->{t2}',end="")
cont = 3
while cont <= termos:
    t3= t1 + t2
    print(f'-->{t3}',end="")
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~' *25)
