#Ler o salário do funcionário e mostrar o aumento de 15%
salario_inicial = float(input('Qual o seu salário? R$ '))
taxa = 15/100 #15%
aumento_salario = salario_inicial+(salario_inicial*taxa)
print(f'O Salário inicial era de R$ {salario_inicial} após aumento de 15% será R$ {aumento_salario}')