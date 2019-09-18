n = int(input('Digite o número da tabuada que quer ver:'))

for c in range(0,11):
    print('{} x {} = {}'.format(c, n, c*n))