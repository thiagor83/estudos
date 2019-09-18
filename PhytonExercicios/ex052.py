n = int(input('Digite um número:'))

for c in range(1, 100):
    if n % c == 1:
        print('O número {}, é primo!'.format(n))
print('O número {}, não é primo!'.format(n))