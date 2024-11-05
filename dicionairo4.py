tradutor = {}
tradutor = {'pineapple':'abacaxi','apple':'maçã','orange':'laranja'}
print(tradutor)
del(tradutor['apple'])
print(tradutor)
print(tradutor.pop('apple','Fruta não encontrada'))