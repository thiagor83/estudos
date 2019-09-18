from datetime import date

nascimento = int(input('Digite o ano de seu nascimento: '))
today = date.today()
dif = today.year - nascimento

if dif <= 9:
    print('MIRIM')
elif dif > 9 and dif <= 14:
    print('INFANTIL')
elif dif > 14 and dif <= 19:
    print('JUNIOR')
elif dif > 19 and dif <= 20:
    print('SENIRO')
else:
    print('MASTER')