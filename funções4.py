
def calcular_pagamento(qtd_horas,valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario=horas*taxa
    else:
        h_exced = horas-40
        salario=40*taxa+(h_exced*(1.5*taxa))
    print(salario)
x = float(input("Digite a quantidade de horas qwu vc trabalha por semana: "))
y= float(input("Digite o quanto vc ganha por hora: "))
calcular_pagamento(x,y)