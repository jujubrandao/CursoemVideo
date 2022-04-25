p = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {p}km')
a = (p*0.50)
b = (p*0.45)
if p < 200:
    print(f'E o preço da sua passagem será de {a}')
else:
    print(f'E o preço da sua passagem será {b}')

