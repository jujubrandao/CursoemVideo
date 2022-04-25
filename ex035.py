print('-=-' *20)
print('Analisador de Triângulos')
print('-=-' *20)
# lados do triângulo: a, b, c
# condição de existência: a < b + c, b < a + c, c < a + b

a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima formam um triângulo')

else:
    print('Os segmentos acima NÃO formam um triângulo')


