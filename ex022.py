n = str(input('Digite seu nome completo: '))
print('Analisando o seu nome...')
mai = n.upper()
print('Seu nome em maiúsculas é {}'.format(mai))
min = n.lower()
print('Seu nome em minúsculas é {}'.format(min))
t = n.replace(' ', '')
t1 = len(t)
print('Seu nome tem ao todo {} letras'.format(t1))
l = n.split()
print('Seu primeiro nome é {} e tem {} letras'.format(l[0], len(l[0])))