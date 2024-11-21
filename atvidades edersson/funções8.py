def cadastro():
    name=input('Qaul seu nome?: ')
    age=int(input("idade: "))
    return name,age

print("inciando cadastro...")
nome,idade = cadastro ()
print("Cadastro realizado com sucesso: ")
print("Seu nome é",nome,'e você tem',idade,'anos de vida')