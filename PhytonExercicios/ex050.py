s = 0
for c in range(1, 7):
    n = int(input("Digite um número, irei somar ele se for par:"))
    if n % 2 == 0:
        s += n
    else:
        continue
print('A somatória de todos os valores foi {}'.format(s))