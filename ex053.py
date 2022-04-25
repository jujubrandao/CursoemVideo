frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(f'Você digitou a frase {frase}')
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
#print(junto, inverso)
if inverso == junto:
    print('Aqui há um palíndromo!')
else:
    print('Não há um palíndromo aqui.')

