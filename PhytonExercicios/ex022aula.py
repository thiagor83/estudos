frase = 'Curso em Video Python'
#string numeração
#C u r s o   e m   V i  d  e  o     P  y   t  h  o  n
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

#imprime letra 9 da variavel frase
print(frase[9])

#imprime letra 9  até o 13 pois o 14  não entra
print(frase[9:14])

#imprime letra 9  até o 21 pulando de 2 em 2 o 21 não entra para no 20.
print(frase[9:21:2])

#imprime do inicio pois você nao setou até o 5.
print(frase[:5])

#imprime do inicio pois você nao setou até o 5.
print(frase[:5])

#Pega o tamanho da frase ou seja o número de caracteres contando os zeros.
print(len(frase))

#Conta quantas vezes existe letra 'o' na frase
print(frase.count('o'))

#Conta quantas vezes existe letra 'o' na frase do Zero ao Doze porque o treze não entra.
print(frase.count('o',0,13))

#Procura em frase a palavra 'deo' e mostra onde inicia, se ele não encontrar ele retorna -1.
print(frase.find('deo'))

#Procura palavra e retorna True ou False
print('Curso' in frase)

#Substitui a palavra Pyton por Android na frase.
print(frase.replace('Python','Android'))

#Transforma em maiusculo, minusculo e a primeira maiuscula ou todas primeiras em maiuscula.
print('{}\n{}\n{}\n{}'.format(frase.upper(),frase.lower(),frase.capitalize(),frase.title()))

frase2 = '   Aprenda Python  '
#Remove espaços inicio e fim como o Trim
print(frase2.strip())

#Remove espaços da direita da frase
print(frase2.rstrip())

#Remove espaços da esquerda da frase
print(frase2.lstrip())

#Divide a frase onde tem espaço criando uma lista
print(frase.split())

#Insere - entre as palavras
print('-'.join(frase.split()))

#Exibe a frase como esta na tela
print("""
Ola
Meu
Nome
é
João
""")

#Combinando funçòes
print(frase.upper().count('o'))

#Combinando funçòes
print(len(frase.strip()))

#Trabalhando a lista do split
dividido = frase.split()
print(dividido[2])

#Trabalhando a lista do split pegando a letra 3 da parte 2 da divisao
dividido = frase.split()
print(dividido[2][3])