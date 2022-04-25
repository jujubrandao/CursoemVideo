somaidade = 0
médiaidade = 0
maioridadehomem = 0
homemaisvelho = 0
totmulher20 = 0
for pessoa in range(1, 5):
    tit= str(input(f'----- {pessoa}ª PESSOA ------'))
    print(tit)
    nom = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        homemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        homemaisvelho = nom
    if sexo in 'Fm' and idade < 20:
        totmulher20 += 1

médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade} anos.')
print(f'O homem mais velho se chama {homemmaisvelho} e tem {maioridadehomem} anos.')
print(f' As mulheres com menos de 20 anos são {totmulher20}.')

