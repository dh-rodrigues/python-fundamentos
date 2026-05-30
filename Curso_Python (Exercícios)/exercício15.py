#Programa que pede quantos dias um carro foi alugado e quantos Km ele percorreu, calcular o valor a ser cobrado sendo que 1 dia=60 reais e 0,15 por Km percorrido
numero_dias = int(input('Quantos dias o carro foi alugado? '))
km_percorrido = float(input('Quantos Km o carro percorreu? '))
valor_cobrado = (numero_dias*60) + (km_percorrido*0.15)
print(f'O valor a ser cobrado considerando {numero_dias} dias e {km_percorrido} Km percorridos é de R$ {valor_cobrado:.2f}')