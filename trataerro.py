try:
    a=int(input("digite uma palavra: "))
except ValueError:
    print("Digite apenas números")
except:
    print("Erro desconhecido")
finally:
    print("Final do algoritmo")
