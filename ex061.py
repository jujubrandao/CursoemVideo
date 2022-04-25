print('Gerador de PA')
print('-==-' *10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
termo = primeiro
while cont <= 10:
    print(f'{termo}--> ',end=" ")
    termo += razão
    cont += 1
print('FIM')
