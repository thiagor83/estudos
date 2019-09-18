nome = str(input('Digite seu nome completo:')).strip()#remove espaço inicio e fim
print(nome.replace(' ',''))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))#Conta as letras e subitrai a quantidade de espaço
print('Seu nome tem {} letras'.format(len(nome.replace(' ',''))))#Quantidade de Caracteres sem espaço.
dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format( (nome.split())[0], len(nome.split()[0]) ))
#mesma coisa que o de cima porem sem criar a variavel dividido.
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0],len(dividido[0])))