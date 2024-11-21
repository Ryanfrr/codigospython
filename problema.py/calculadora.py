import adicao
import subtração
import multiplicação
import divisão

class Calculadora:
    def calcular(opção,num1,num2):
        if opção == 1:
            resultado = adicao.Adicao.adc(num1,num2)
            print( num1 ,'+',num2, '=', resultado)
        elif opção ==2:
            resultado = subtração.Subtracao.subt(num1,num2)
            print( num1 ,'-',num2, '=', resultado)
        elif opção ==3:
            resultado = multiplicação.Multiplicação.mult(num1,num2)
            print( num1 ,'x',num2, '=', resultado)
        elif opção == 4:
            resultado = divisão.Divisao.div(num1,num2)
            print( num1 ,'/',num2, '=', resultado)
        return resultado