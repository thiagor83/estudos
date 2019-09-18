km = float(input('Quanto você rodou com o carro? km'))
dias = int(input('Quantos dias você ficou com o carro?'))
custo = (dias * 60) + (km * 0.15)
print(' Você ficou {} dias com o carro \n Rodou {}KM \n O valor a pagar é R$ {:.2f}'.format(dias,km,custo))