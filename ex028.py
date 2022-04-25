print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
import random
num = int(input('Em que número eu pensei? '))
from time import sleep
print('PROCESSANDO...')
sleep(2)
num_sort = random.randint(0, 5)
print(num_sort)
if num_sort == num:
    print(f'PARABÉNS! Eu também pensei no número {num}.')
else:
    print(f'GANHEI! Eu pensei no número {num_sort} e não no {num}.')
