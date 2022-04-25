peso = float(input('Qual o seu peso? (kg;) '))
altura = float(input('Qual a sua altura? (m;) '))
IMC = peso / (altura * altura)
print(f'O IMC dessa pessoa é {IMC}')
if IMC < 18.5:
    print('Eita, você está abaixo do PESO IDEAL.')
    print('Pode comer mais besteira.')
elif 18.5 < IMC <25:
    print('Parabéns! Você está no seu PESO IDEAL.')
    print('Mantenha assim.')
elif 25 < IMC < 30:
    print('Você está com SOBREPESO.')
    print('Faça um treininho de leve e coma melhor.')
elif 30 < IMC < 40:
    print('Poxa, você está OBESO(A).')
    print('Que tal uma mudança de estilo de vida? Já pensou nisso?')
else:
    print('Opa, OBESIDADE MÓRBIDA.')
    print('Tudo bem. Você já pensou em fazer um acompanhamento multidisciplinar?')
    print('Seus marcadores podem se alterar e diminuir sua qualidade de vida com o tempo.')