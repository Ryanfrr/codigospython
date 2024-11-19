def busca_binaria(lista,elemento):
    baixo = 0
    alto = len(lista)-1
    while baixo <= alto:
        meio = (baixo+alto)//2
        if lista[meio]==elemento:
            return meio
        elif lista[meio]<elemento:
            baixo = meio +1
        else:
            alto = meio -1
    return -1