#Programa para pedir a temperatura em graus celsius e mostrar sua correspondente em graus fahrenheit e kelvin
graus_celsius = float(input('Qual a temperatura em °C?'))
graus_fahrenheit = (graus_celsius*1.8)+32
kelvin = graus_celsius+273
print(f'A temperatura de {graus_celsius} °C, corresponde a {graus_fahrenheit} °F e {kelvin} K')