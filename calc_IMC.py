
nome = input('digite seu nome:')
altura = float(input('digite sua altura:'))
peso = float(input('digite seu peso:'))
imc = peso / (altura ** 2)

resultado = round(imc,2)

if imc < 18.5:
    print('abaixo do peso')
    print('')
    print('come mais mano')
elif imc < 25:
    print('peso normal') 
    print('')
    print('boaaa')
elif imc < 30:
    print('sobrepeso')
    print('')
    print('ou vc manera ou vou te confudir com uma bola um dia')
elif imc <35:
    print('obesidade grau 1')
    print('')
    print('quer xtudo, quer xbacon...')
elif imc <35:
    print('obesidade grau 2')
    print('')
    print('dá tempo de mudar')
else:
    print('obesidade grau 3 (mórbida)')
    print('não siga o exemplo da Thais Carla!!')
print(resultado)
