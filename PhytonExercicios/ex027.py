nome = str(input('Digite seu nome completo: ')).strip()
nome2 = nome.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome2[0]))
print('Seu último nome é {}'.format(nome2[len(nome2)-1]))
