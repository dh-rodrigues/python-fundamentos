#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
primeiro_numero = int(input('Qual o primeiro número a ser analisado: '))
segundo_numero = int(input('Qual o segundo número a ser analisado: '))
terceiro_numero = int(input('Qual o terceiro número a ser analisado: '))

#Análise do maior número
if primeiro_numero >= segundo_numero and primeiro_numero >= terceiro_numero:
    print(f'O maior número informado foi {primeiro_numero}')
elif segundo_numero >= primeiro_numero and segundo_numero >= terceiro_numero:
    print(f'O maior número informado foi {segundo_numero}')
else:
    print(f'O maior número informado foi {terceiro_numero}')

#Análise do menor número 
if primeiro_numero <= segundo_numero and primeiro_numero <= terceiro_numero:
    print(f'O menor número informado foi {primeiro_numero}')
elif segundo_numero <= primeiro_numero and segundo_numero <= terceiro_numero:
    print(f'O menor número informado foi {segundo_numero}')
else:
    print(f'O menor número informado foi {terceiro_numero}')

#Outra opção utilizando Biblioteca
#maior = max(primeiro_numero, segundo_numero, terceiro_numero) 
#menor = min(primeiro_numero, segundo_numero, terceiro_numero)
#print(f'O maior número informado foi {maior}')
#print(f'O menor número informado foi {menor}')