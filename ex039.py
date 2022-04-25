ano = int(input('Ano de nascimento: '))
print(f'Quem nasceu em {ano} tem {2022 - ano} anos em 2022')
if (2022 - ano) < 18:
    print(f'Ainda faltam {18 -(2022 -ano)} anos para o alistamento')
    print(f'Seu alistamento será em {18 - (18 -(2022 - ano))}')
elif (2022 - ano) > 18:
    print(f'Você já deveria ter se alistado há {(2022 - ano) - 18} anos')
    print(f'Seu alistamento foi em {2022 - ((2022 - ano) - 18)}')
else:
    print('Quem nasceu em 2004 tem 18 anos agora!')
    print('Você tem que se alistar IMEDIATAMENTE!')

    