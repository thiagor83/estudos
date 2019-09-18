s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
    else:
        continue
print('A somatória de todos os valores foi {}'.format(s))