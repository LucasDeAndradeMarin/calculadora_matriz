from matriz import *
from matriz.matriz2 import *
from matriz.matriz3 import *

while True:
    tamanho = int(input('Qual o tamanho da sua matriz? ?x? OBS: Digite apenas uma vez o valor! '))
    if tamanho == 2:
        matriz = matriz2()
    elif tamanho == 3:
        matriz = matriz3()
    else:
        print('''Infelizmente nossa calculadora ainda não suporta matrizes não-quadradas e matrizes quadradas maiores que 3. 
        Porém estamos trabalhando diariamente para melhorar a sua experiência aqui!!''')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja fazer outra conta? [S/N]  ')).strip().upper()[0]
    if cont in 'N':
        break


