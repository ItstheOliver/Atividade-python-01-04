#exercício 2

turno = input('Digite o turno que trabalha (M/N): ')
horas_trabalhadas = int(input('Digite sua horas trabalhadas: '))

if turno == 'N':
    valor_hora = 45.00
else:
    valor_hora = 37.50

salario = valor_hora * horas_trabalhadas

print('O valor do salário é:', salario)