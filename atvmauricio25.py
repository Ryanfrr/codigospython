def remove_duplicados(lista):
    return list(set(lista))
numeros = [1,2,3,4,5,6,7,7,7,7,7,7]
print(remove_duplicados(numeros))