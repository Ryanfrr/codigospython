def conta_consoantes(texto):
    consoantes = 'bcdfghjklmnopqrstvwxyz'
    texto = texto.lower()
    contador = 0
    for letra in texto:
        if letra in consoantes:
            contador += 1
    return contador