#Exercício 1

import math
altura = float(input('Qual a altura da pirâmide: '))
basemenor = float(input('Qual a base menor da pirâmide: '))
basemaior = float(input('Qual a base maior da pirâmide: '))
volume = altura/3*(basemaior**2 + basemenor**2 +(basemaior**2*basemenor**2)**0.5)

print('O volume do tronco da pirâmide é: ', volume)