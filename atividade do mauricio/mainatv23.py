def multiplica_pares(lista):
    produto=1
    for num in lista:
        if num %2 ==0:
            produto*=num
    return produto