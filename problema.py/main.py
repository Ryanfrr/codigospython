import calculadora

while True:
    print("=-="*15)
    print("Calculadora")
    print("=-="*15)
    print("0 - Sair")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    while True:
        try:
         opção = int(input("Digite a operação desejada: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        else:
            break
    if opção == 0:
        print("Saindo...")
        break
    elif opção != 1 and opção != 2 and opção != 3 and opção != 4:
        print("Opção invalida!")
        continue
    
    while True:
        try:
            num1 = int(input("Digite um número: "))
        except ValueError:
            print("Digite apenas números!")
        else:
            break
    while True:
        try:
            num2 = int(input("Digite um número: "))
        except ValueError:
            print("Digite apenas números!")
        else:
            if opção == 4 and num2 == 0:
                print(f"{num1} não pode ser dividido por zero!")
                continue
            break
    print("=-="*15)

    total = calculadora.Calculadora.calcular(opção,num1,num2)