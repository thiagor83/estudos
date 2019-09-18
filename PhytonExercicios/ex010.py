n1 = float(input('Quanto dinheiro você tem ai mano? R$'))
n2 = float(input('Qual a cotação do dolar hoje?'))
print('Com R${:.2f} reais, você consegue comprar ${:.2f} dolares!'.format(n1,(n1/n2)))
