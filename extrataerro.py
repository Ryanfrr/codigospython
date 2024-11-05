import os
while True:
    try:
        num1 = float(input('Digite um numero: '))
        num2 = float(input('Digite um numero: '))
        os.system('cls')
    except ValueError:
            print('Digite apenas numeros')
            continue
    cal = int(input("informe o calculo \n 1) adc \n2)subt\n3)mult\n4)div"))
    calf = 0
    if cal ==1:
            calf = num1 + num2
            print ('resultado: ',calf)
           
    if cal ==2: 
            calf = num1- num2
            print ('resultado: ',calf)
           
    if cal ==3:
            calf = num1 * num2
            print ('resultado: ',calf)  
           
    try:      
        if cal ==4:
                calf = num1 /num2
                print ('resultado: ',calf)
    except ZeroDivisionError:
                print("Não é possivel dividir por 0")
                continue



  