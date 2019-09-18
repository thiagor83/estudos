peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
res = peso / (altura ** 2)
if res < 18.5:
    print('{:.0f} Abaixo do Peso!'.format(res))
elif res >= 18.5 and res <= 25:
    print('{:.0f} Peso ideal!'.format(res))
elif res > 25 and res <= 30:
    print('{:.0f} Sobrepeso!'.format(res))
elif res > 30 and res <= 40:
    print('{:.0f} Obesidade'.format(res))
else:
    print('{:.0f} Obesidade Morbida!'.format(res))