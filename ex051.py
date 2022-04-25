print(15* '==')
print('10 TERMOS DE UMA PA')
print(15* '==')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
#enésimo termo de uma PA = décimo termo = primeiro +(10 -1) * razão
décimo = primeiro + (10 -1) * razão
for termo in range(primeiro, décimo + razão, razão):
    print(f'{termo}', end=" -> ")
print('Acabou')