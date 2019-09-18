a = input('Digite algo:')
if a.isnumeric() == True:
    print('O valor digitado é númerico!')
if a.isalnum() == True:
    print('O valor digitado é alfa númerico!')
if a.isalpha() == True:
    print('Todos valores são alfabeticos!')
if a.isdecimal() == True:
    print('Todos valores é decimal!')
if a.isdigit() == True:
    print('Todos valores é digito!')
if a.isidentifier() == True:
    print('Todos valores é identificador!')
if a.islower() == True:
    print('Todos valores é minusculo!')
if a.isprintable() == True:
    print('Todos valores imprimivel!')
if a.isspace() == True:
    print('Todos valores é só espaço!')
if a.istitle() == True:
    print('Todos valores é título!')
if a.isupper() == True:
    print('Todos valores é maiusculo!')