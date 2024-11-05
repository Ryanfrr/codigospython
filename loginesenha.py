def validarsenha(senha):
    if len(senha) < 8:
        return False
    temmaiuscula = any(c.supper() for c in senha)
    temminuscula = any(c.islower() for c in senha)
    temnumero = any(c.isdigit() for c in senha)
    return temmaiuscula and temminuscula and temnumero

def main():
    while True:
        login = input("Login = ")
        senha = input("Senha = ")

        if validarsenha(senha):
            print("Conta logada com sucesso!")
            break
        else:
            print("Login ou senha invalido, tente novamente!")

main()