preco = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o valor do desconto em %:'))
valorfinal = preco - ((desconto * preco) / 100)
print('O valor do produto é R${:.2f}, o valor do desconto é {}%, o valor com o desconto é R${:.2f}.'.format(preco,desconto,valorfinal))