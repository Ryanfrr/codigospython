def conta_intervalo(lista,inicio,fim):
    return sum(1 for num in lista if inicio <= num <= fim)