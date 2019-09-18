salario = float(input('Digite o salário do Renan: R$'))
aumento = float(input('Digite o valor do aumento em %:'))
salariocorrigido = salario + ((salario * aumento)/100)
print('O salário do Renan hoje é R$ {:.2f}, com o aumento passará a ser R$ {:.2f}'.format(salario, salariocorrigido))