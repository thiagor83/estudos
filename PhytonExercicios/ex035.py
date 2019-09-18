r1 = float(input('Digite o valor 1: '))
r2 = float(input('Digite o valor 2: '))
r3 = float(input('Digite o valor 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo!')
else:
    print('Os segmentos NÃO podem formar um triangulo!')
