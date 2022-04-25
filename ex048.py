soma = 0 #acumulador
cont = 0 #contador
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 #cont += 1
        soma = soma + c #soma += c
print(f'A soma de todos {cont} valores solicitados é {soma}')
