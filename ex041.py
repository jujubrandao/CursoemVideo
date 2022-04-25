ano = int(input('Digite seu ano de nascimento: '))
print(f'Você tem {2022 - ano} anos')
if (2022 - ano) <= 9:
    print('Você pertence à categoria MIRIM!')
elif (2022 - ano) <= 14:
    print('Você pertence à categoria INFANTIL!')
elif (2022 - ano) <= 19:
    print('Você pertence à categoria JÚNIOR!')
elif (2022 - ano) <= 25:
    print('Você pertence à categoria SÊNIOR!')
else:
    (2022 - ano) > 25
    print('Você pertence à categoria MASTER!')
