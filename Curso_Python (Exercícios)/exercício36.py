#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('\033[1;37;40m                $ SIMULAÇÃO DE EMPRÉSTIMO $                \033[m')
casa = float(input('\033[;33;44mQual o valor da casa que você deseja comprar?\033[m R$'))
salario = float(input('\033[;33;44mQual o seu salário atual?\033[m R$ '))
anos_pagamento = int(input('\033[;33;44mEm quantos anos deseja realizar o pagamento?\033[m R$ '))