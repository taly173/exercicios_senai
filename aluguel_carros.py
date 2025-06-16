# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

#1 - (dias) Pedir a quantidade de dias
#2 - (km) Pedir a quantidade de km percorridos
#4 - (valor_km) Calcular o valor total da quilometragem (km * 0.15)
#5 - (valor_total) Calcular o valor total somando o valor dos dias + o valor dos km
#6 - Mostrar na tela a frase formatada

carro=input('qual carro foi alugado':)
dias=int(input('quantidade de dias de uso:'))
km=float(input('quantos km percorridos:'))
valor_dias = dias* 60
valor_km=km*0.15
valor_total= valor_dias+valor_km

print(f'você andou {km} por{dias} o valor que você tem que pagar é{valor_total}')

