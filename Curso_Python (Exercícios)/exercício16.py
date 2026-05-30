# Programa que leia um número real e mostre na tela somente a parte inteira dele utilizando biblioteca math
import math
numero = float(input('Digite um número real: '))
print(f'O número digitado foi {numero}, sua parte inteira é', math.trunc(numero))
