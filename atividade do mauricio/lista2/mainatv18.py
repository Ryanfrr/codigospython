def media_poderada(lista_valores,lista_pesos):
    if len(lista_valores)!=len(lista_pesos):
        raise ValueError('as listas devem ter o mesmo tamanho')
    soma_pesos = sum(lista_pesos)
    if soma_pesos == 0:
        raise ValueError('a soma dos pesoas não pode ser zero ')
    soma_poderada = sum(valor*peso for valor,peso in zip(lista_valores,lista_pesos))
    return soma_poderada/soma_pesos