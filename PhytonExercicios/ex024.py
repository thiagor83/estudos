cidade = str(input('Digite a cidade em que você nasceu:')).strip()
particionado = cidade.split()
print('santo' in (particionado[0]).lower())
print(cidade[:5] == 'Santo') #pega os 5 primeiros caracteres e valida se é igual Santo