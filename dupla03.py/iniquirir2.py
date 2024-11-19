from InquirerPy import inquirer

def valida_email(voL):
    if '@' not in voL:
        raise ValueError('pro favor, insira um email valido')
    return voL
email= inquirer.text('Qual é o seu email?',validate=valida_email).execute()