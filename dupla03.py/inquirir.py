from InquirerPy import inquirer

nome = inquirer.text('qual é o seu nome?').execute()
cor= inquirer.select('qual é a sua cpr favorita?',
                    choices =['azul','verde','vermelho']).execute() 