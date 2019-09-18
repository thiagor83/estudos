vel = int(input('Qual a velocidade atual do carro? '))
limite = 80
if vel > limite:
    print('Multado! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R$ {:.2f}'.format((vel-limite)*7.00))
print('Tenha um bom dia, digija com cuidado!')