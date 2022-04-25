from datetime import date
atual = date.today().year
totmaior =0
totmenor =0
for pessoa in range(1 , 8):
    nasc = int(input(f'Em que ano nasceu a {pessoa}ª pessoa? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior +=1
    else:
        totmenor +=1
print(f'Ao todo, temos {totmaior} pessoas MAIORES de idade.')
print(f'Assim como temos {totmenor} pessoas MENORES de idade.')



