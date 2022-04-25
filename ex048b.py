s=0
for n in range(1, 500, 2):
    if n % 3 == 0:
        print(n, end= ' ')
        s+=n

print(f'\nA soma de todos esses valores, múltiplos de três, é igual a {s}')
