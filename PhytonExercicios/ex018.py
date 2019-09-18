import math
an = float(input('Digite o Angulo que você deseja:'))
#radians converte para radiano
#sin função do math para seno
#cos função do math para coseno
#tan função do math para tangente
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(seno,cos,tan))