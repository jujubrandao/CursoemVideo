p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))
lista = ['p','s','t']
if p < s and p < t:
    print(f'O menor valor digitado foi {p}')
if s < p and s < t:
    print(f'O menor valor digitado foi {s}')
if t < p and t < s:
    print(f'O menor valor digitado foi {t}')
if p > s and p > t:
    print(f'O maior valor digitado foi {p}')
if s > p and s > t:
    print(f'O maior valor digitado foi {s}')
if t > p and t > s:
    print(f'O maior valor digitado foi {t}')
