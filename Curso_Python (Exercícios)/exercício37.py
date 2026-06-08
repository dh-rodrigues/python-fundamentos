#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('\033[1;37;40m                CONVERSOR DE BASES NUMÉRICAS                \033[m')
inteiro = int(input('Qual número inteiro você deseja converter?\n'))
escolha = int(input('Digite 1 para converter para binário\nDigite 2 para converter para octal\nDigite 3 para converter para hexadecimal\n'))  
if escolha == 1:
    print(bin(inteiro)[2:])
elif escolha == 2:
    print(oct(inteiro)[2:]) 
elif escolha == 3:
    print(hex(inteiro)[2:])
else:
    print(f'O número {escolha} não é uma opção válida')
