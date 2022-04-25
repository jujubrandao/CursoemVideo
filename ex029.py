v = int(input('Qual é a velocidade atual do carro? '))
m = (v - 80) * 7
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de {m}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')