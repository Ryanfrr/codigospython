def troca_vogais(s,nova_letra):
    vogais = 'aeiouAEIOU'
    return''.join([nova_letra if c in vogais else c for c in s])
print(troca_vogais("Gilberto cuzudo",'b'))