def soma_naturais(n):
    if n <1:
        raise ValueError('N deve ser um numero natural positivo')
    return n *(n+1)//2