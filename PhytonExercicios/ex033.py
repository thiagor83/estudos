a = int(input('Primeiro Número:'))
b = int(input('Segundo Número:'))
c = int(input('Terceiro Número:'))
menor = a
if b<a and b<c:
    menor = n2
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O número menor foi {}'.format(menor))
print('O número maior foi {}'.format(maior))