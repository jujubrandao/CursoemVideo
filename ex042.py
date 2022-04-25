p = int(input('Pirmeiro segmento: '))
s = int(input('Segundo segmento: '))
t = int(input('Terceiro segmento: '))
#condição de existência: p < s + t and s < p + t and t < p + s
if p == s == t:
    p < s + t and s < p + t and t < p + s
    print('Ói, esse triângulo é EQUILÁTERO!')
elif p == s or p == t:
    p < s + t and s < p + t and t < p + s
    print('Mhmmm, esse triângulo é ISÓSCELES!')
else:
    p < s + t and s < p + t and t < p + s
    print('Aiai, o triângulo é ESCALENO!')
