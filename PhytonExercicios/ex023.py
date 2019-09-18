num = int(input('Informe um número: '))
u = num // 1 % 10 # divisão inteira por 1 e pega o resto
d = num // 10 % 10 # divisão inteira por 10 e pega o resto
c = num // 100 % 10 # divisão inteira por 100 e pega o resto
m = num // 1000 % 10 # divisão inteira por 1000 e pega o resto
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))