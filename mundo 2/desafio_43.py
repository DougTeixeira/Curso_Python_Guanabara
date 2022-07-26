peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Vc está a baixo do peso ideal, {}.'.format(imc))
elif imc < 25.0:
    print('Vc está no peso ideal. {}.'.format(imc))
elif imc < 30.0:
    print('Vc está com sobrepeso. {}.'.format(imc))
elif imc > 40.0:
    print('Vc está com obesidade mórbida. {}.'.format(imc))
else:
    print('Valor ou valores invalidos.')
