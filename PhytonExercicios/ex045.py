import random

escolha = 0

while escolha <= 0 or escolha >= 3:

    escolha = int(input('Escolha as opções abaixo: \n 1 - PAPEL\n 2 - TESOURA\n 3 - PEDRA\n'))


    if escolha == 1:
        print('Você escolheu PAPEL!')
        textoescolha = 'PAPEL'
    elif escolha == 2:
        print('Você escolheu TESOURA!')
        textoescolha = 'TESOURA'
    elif escolha == 3:
        print('Você escolheu PEDRA!')
        textoescolha = 'PEDRA'
    else:
        print('Número inválido seu BURRO!')
        print('{:=^40}'.format(''))
        continue

    sort = random.randint(1,3)

    if sort == 1:
        print('O computador escolheu PAPEL!')
        escolhapc = 'PAPEL'
    elif sort == 2:
        print('O computador TESOURA!')
        escolhapc = 'TESOURA'
    elif sort == 3:
        print('O computador PEDRA!')
        escolhapc = 'PEDRA'

    if escolha == sort:
        print('EMPATE')
        escolha = 0
        print('{:=^40}'.format(' VAMOS DE NOVO '))
    elif (escolha == 1 and sort == 2) or (escolha == 2 and sort == 3) or (escolha == 3 and sort == 1):
        print('Você perdeu seu RUIM!!!')
    else:
        print('{:=^40}'.format(' PARABÉNS Você Ganhou, FIM DE JOGO '))

