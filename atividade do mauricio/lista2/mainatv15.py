def multiplica_matrizes(matriz1,matriz2):
    if len(matriz1)!=2 or len(matriz1[0])!=2 or len(matriz2)!=2 or len(matriz2[0])!=2:
        raise ValueError('As matrizes devem ser 2x2')
    resultado = [[0,0],[0,0]]
    for i in range(2):
        for j in range (2):
            for k in range (2):
                resultado[i][j]+=matriz1[i][k]*matriz2[k][j]
    return resultado