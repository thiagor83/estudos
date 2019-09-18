altura = float(input('Altura da parede:'))
largura = float(input('Largura da parede:'))
area = altura * largura
print('Você vai precisar de {}lts de tinta para pintar sua parede de {}mts quadrado(s).'.format(area/2,area))