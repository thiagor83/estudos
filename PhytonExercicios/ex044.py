print('{:=^40}'.format(' THIAGO '))

for c in range(1, 6): #conta de 1 a 5 porque no 6 sai do laço
    print(c)
print("Fim")

for c in range(6, 0, -1): #conta de 6 a 1 ou seja voltando número e para no 1 porque no 0 sai do laço
    print(c)
print("Fim")

for c in range(0, 7, 2): # conta de 0 a 6 de dois em dois
    print(c)
print("Fim")

#recebe o número de até onde deve ir
n = int(input('Digite um número'))
for c in range(0, n+1):
    print(c)

#recebe inicio, fim e o passo de quanto em quanto pula
i = int(input('Digite o inicio:'))
f = int(input('Digite o fim:'))
p = int(input('Digite o passo:'))
for c in range(i, f+1, p):
    print(c)

#laço somando valores digitados
s = 0
for c in range(0, 4):
    n2 = int(input('Digite um Valor:'))
    s += n2
print('A somatória de todos os valores foi {}'.format(s))