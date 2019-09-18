n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Você foi reprovado!')
elif media >= 5 and media <= 6.9:
        print('Você esta de recuperação!')
else:
    print('Você esta aprovado!')