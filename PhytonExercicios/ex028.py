from random import randint
from time import sleep
print('Vou pensar em um número...')
sleep(4)
print('-=-' * 20)
n = int(input('Pensei em um número de 0 a 5, qual foi?' ))
print('-=-' * 20)
n2 = randint(0,5) #Sorteia um número de 0 a 5.
if n2 == n:
    print('Muito bem você acertou!')
else:
    print('Ops você errou! eu pensei no número {}'.format(n2))