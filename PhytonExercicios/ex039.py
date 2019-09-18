idade = int(input('Digite sua idade: '))
if idade == 18:
    print('Esta na hora de se alistar no exercito!')
elif idade < 18:
    print('Você ainda não tem idade para se alistar no exercito!\n Ainda faltam {} anos para você se alistar!'.format(18-idade))
else:
    print('Você já passou da idade de se alistar no exercito!\n Esta {} anos atrasado!'.format(idade-18))