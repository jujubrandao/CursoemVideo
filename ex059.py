from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('-=-' *10)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    opção = int(input('>>>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = primeiro + segundo
        print(f'A soma entre {primeiro} e {segundo} é {soma}.')
    elif opção == 2:
        produto = primeiro * segundo
        print(f'O produto entre {primeiro} e {segundo} é {produto}')
    elif opção == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print(f'Entre {primeiro} e {segundo} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente.')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente novamente.')
    print('-=-' * 10)





