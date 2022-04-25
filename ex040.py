p = float(input('Primeira nota: '))
s = float(input('Segunda nota: '))
média = (p + s) / 2
if média >= 7:
    print(f'Tirand {p} e {s} sua MÉDIA é {média}')
    print('PARABÉNS! Você foi aprovado.')
elif 5 < média < 6.9:
    print(f'Tirando {p} e {s} sua média é {média}')
    print('Eita. Você está de recuperação. :-(')
else:
    média < 5
    print(f'Tirando {p} e {s} , sua média é {média}')
    print('Poxa, você foi reprovado! :(')
