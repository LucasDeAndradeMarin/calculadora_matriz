def matriz2():
    '''Matriz 2x2'''
    matriz = [[0, 0], [0, 0]]
    for l in range (0, 2):
        for c in range(0, 2):
            matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    prin = (matriz[0][0] * matriz[1][1])
    sec = (matriz[0][1] * matriz[1][0])
    det = prin - sec
    print('-=-'*30)
    for l in range(0, 2):
        for c in range(0, 2):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()
    print('-=-'*30)
    print(f'Como a diagonal principal equivale à {prin} e a secundária à {sec}, o determinante dessa matriz 2x2 vale {det}')



