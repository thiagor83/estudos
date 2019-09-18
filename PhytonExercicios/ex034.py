salario = float(input('Qual é o salário do Funcionário? '))
aumento = salario * 1.15 if salario <= 1250 else salario * 1.10
print('O salário com aumento é de R$ {:.2f}'.format(aumento))