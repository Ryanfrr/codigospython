import math
def desvio_padrao(lista):
    media = sum(lista)/len(lista)
    varianca = sum((x-media)**2 for x in lista)/len(lista)
    return math.sqrt(varianca)