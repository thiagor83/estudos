nome = str(input('Digite uma Frase: ')).strip().lower()
letra = str(input('Qual letra você quer analisar? ')).strip().lower()
print('A letra {} aparece {} vezes na frase.'.format(letra, nome.count(letra)))
print('A primeira letra {} apareceu na posição {}'.format(letra, nome.find(letra)))
print('A última letra {} apareceu na posição {}'.format(letra, nome.rfind(letra)))
print(nome)