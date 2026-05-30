#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random 
numero = random.randint(0,5)
escolha = int(input("Digite um número de 0 a 5: "))
if numero == escolha:
    print('Parabéns o número escolhido foi o mesmo da máquina')
else:
    print('Você não escoheu o mesmo número que a máquina')
print(f'MAQUINA:{numero}')
print(f'SUA ESCOLHA:{escolha}')