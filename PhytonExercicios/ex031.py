d = float(input('Digite a distancia'))
preço = d * 0.50 if d <= 200 else d * 0.45
print('O custo total da sua viagem é de R$ {:.2f}'.format(preço))