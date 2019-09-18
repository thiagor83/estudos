nome = str(input('Qual seu nome?'))
print('{} você esta querendo finaciar uma casa então?'.format(nome))
vlrcasa = float(input('Qual seria o valor do imóvel?'))
salario = float(input('Legal {}, qual seria o seu salário?'.format(nome)))
anos = int(input('Em quantos anos você quer pagar?'))
nparcelas = anos * 12
print('Bom vamos lá... \n {} você quer comprar uma casa no valor de R$ {:.3f}, com um salário de R$ {}, e pagar em {} parcelas.'.format(nome,vlrcasa,salario,nparcelas))
print('Para isso {} você só pode comprometer 30% do seu salário, ou seja R$ {:.2f}.'.format(nome,(salario*0.3)))
vlrparcela = vlrcasa / nparcelas
maxparcela = salario * 0.3
if vlrparcela > maxparcela:
    print('O valor da parcela esta muito alto, o valor máximo da parcela seria de {}'.format(maxparcela))
elif vlrparcela < maxparcela:
    print('Perfeito {}, vamos fazer o financiamento para você. Então seriam {} de {:.2f} OK?'.format(nome,nparcelas,vlrparcela))
print('Podemos fazer em {} parcelas, {} anos oque acha?'.format(int(vlrcasa/maxparcela),int((vlrcasa/maxparcela)/12)))
