def diagonais_matriz(matriz):
    if len(matriz)!= len(matriz[0]):
        raise ValueError ('a matriz não é quadrada')
    diagonal_principal = [matriz[i][i]for i in range(len(matriz))]
    diagonal_secundaria = [matriz[i][len(matriz)-i-1]for i in range (len(matriz))]
    return diagonal_principal + diagonal_secundaria