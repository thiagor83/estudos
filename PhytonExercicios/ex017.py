import math
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente'))
ch = math.sqrt(pow(co,2)+pow(ca,2))
hi = math.hypot(co, ca)#função hipotenusa do Python
print('O comprimento da hipotenusa é {:.2f}'.format(ch))
print('O comprimento da hipotenusa é {:.2f}'.format(hi))