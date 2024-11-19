def diferenca_max_min(lista):
    if not lista:
        raise ValueError('A lista não pode ser vazia')
    return max(lista)-min(lista)