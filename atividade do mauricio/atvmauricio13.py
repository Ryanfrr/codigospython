def conta_letras(s,letra):
    s =s.lower()
    letra = letra.lower()
    return s.count(letra)
print(conta_letras('Adalberto viado ','a'))
