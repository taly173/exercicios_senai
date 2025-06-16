contador = 0
fim = int(input('vou somar até o número que você pedir. digite um número:'))
soma = 0
while contador <= fim:
    soma = soma + contador
    contador = contador+ 1

print(f'Resultado: {soma}')