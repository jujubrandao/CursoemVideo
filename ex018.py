import math
a = float(input('Digite o ângulo que você deseja: '))

s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('O ângulo de {} tem o SENO de {}'.format(a, s))
print('O ângulo de {} tem o COSSENO de {}'.format(a, c))
print('O ângulo de {} tem a TANGENTE de {}'.format(a,t))
