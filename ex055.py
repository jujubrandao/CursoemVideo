maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso que vemos aqui é {maior}Kg')
print(f'E o menor peso é {menor}Kg')
