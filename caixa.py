total = 0
lista=[]
while True:
    caixa = float(input("Informe um valor:"))
    nome= str(input("Nome do produto: "))
    if caixa >=1:
        total = total + caixa
        print("Produto: ", nome, caixa)
        
    elif caixa == 0:
        break
    else:
        print("Valor invalido")
        
pag=float(input("Informe o valor do pagamento: "))
total1 = pag - total
if pag < total:#errado
    print ("Valor invalido")
    
else:
    print ("\nTotal: ", total)
    print ("Valor do pagamento", pag)
    print ("Troco ", total1)
    for n in nome:
        print(n)
   
