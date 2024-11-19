def produto_escalar(vetor1,vetor2):
    if len(vetor1)!=len(vetor2):
        raise ValueError('Os vetores deven ter o mesmo tamanho')
    return sum(x*y for x,y in zip(vetor1,vetor2))