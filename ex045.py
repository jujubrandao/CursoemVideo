print('Suas opções são: \n[ 1 ] PEDRA \n[ 2 ] PAPEL \n[ 3 ]TESOURA')
jogada = int(input('Qual a sua jogada? '))

from time import sleep
for jogada in range(0,1):
    sleep(2)
    print('JO')
for jogada in range(0, 1):
    sleep(2)
    print('KEN')
for jogada in range(0, 1):
    sleep(2)
    print('PO')

print('-=-=-=-=-=-=-=-=-=-=-')
lista = [1 , 2, 3]
if lista == 1:
    print('PEDRA')
elif lista == 2:
    print('PAPEL')
else:
    print('TESOURA')
import random
aleatorio = random.sample(lista, 1)
k = random.choice(aleatorio)
print(f'Computador jogou {k}')
lista2 = [1, 2, 3]
x = random.choice(lista2)
print(f'Jogador jogou {x}')
print('-=-=-=-=-=-=-=-=-=-=-')
#vence quem:
if pc == pedra and jogador == pedra:
    print('EMPATE')
elif pc == pedra and jogador == tesoura:
    print('PC VENCE')
elif pc == pedra and jogador == papel:
    print('PC VENCE')
elif 
#print(f'{} VENCE')