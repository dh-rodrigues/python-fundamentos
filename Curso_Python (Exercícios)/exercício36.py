#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('\033[1;37;40m                $ SIMULAÇÃO DE EMPRÉSTIMO $                \033[m')
valor_casa = float(input('Qual o valor da casa que você deseja comprar? R$'))
salario = float(input('Qual o seu salário atual? R$ '))
anos_pagamento = int(input('Em quantos anos deseja realizar o pagamento? '))
prestacao_mensal = valor_casa/(anos_pagamento*12) #tranforma ano em meses e divide do valor da casa
if prestacao_mensal > 0.3*salario:
    print(f'\033[;37;41mEMPRÉSTIMO NEGADO\033[m \nO valor da prestação mensal é R${prestacao_mensal:.2f} o que excede 30% do seu salário')
else:
    print(f'\033[;37;42mEMPRÉSTIMO CONCEDIDO\033[m \nO valor da prestação mensal é R${prestacao_mensal:.2f} o que é menor que 30% do seu salário.')