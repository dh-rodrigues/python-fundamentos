#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input('Digite um número de 0 a 9999: '))
milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10
print(f'O milhar deste numero é: {milhar}')
print(f'O centena deste numero é: {centena}')
print(f'O dezena deste numero é: {dezena}')
print(f'A unidade deste numero é:{unidade}')