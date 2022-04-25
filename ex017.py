from math import sqrt
o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
h = o*o + a*a
# hi = math.hypot(co, ca)

print('A hipotenusa vai medir {}'.format(sqrt(h)))

