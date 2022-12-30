login_usuario = []
senha_usuario = []
login = []
database = {}


def menu():
    print('------------------')
    print(f'{"    LOGIN    "}')
    print('------------------')
    print("""
    \n\t[1] ENTRAR
    \n\t[2] REGISTRAR
    \n\t[3] SAIR
    """)
   

def entrar():
    for i in range(10):
        username = str(input('\nLogin: '))
        while username in login:
            print('\n Usuário não encontrado! \nTente novamente...')
            username = str(input('\nLogin: '))
        password = str(input('Senha: '))
        while len(password) < 6:
            print('\nSenha curta!\nTente novamente, sua senha deve conter ao menos seis caractere ...')
            password = str(input('\Senha: '))
        login_usuario.append(username)
        senha_usuario.append(password)
        database['Username'] = username
        database['Senha'] = password
        login.append(database.copy())
        database.clear()


def registrar():
    database['Login'] = str(input('\nDigite seu login: '))
    database['Senha'] = str(input('Digite sua senha: '))
    if database not in login:
        print('\nFalha na autenticação!\nTente novamente...')
    else:
        print(f"\nSucesso na autenticação!\nBem-vindo(a), {database['Login']}")
    
    
while True:
    menu()
    option = int(input('\nEscolha uma opção: '))
    if option == 1:
        entrar()
    elif option == 2:
        registrar()
    elif option == 3:
        print('Saindo...')
        break
    else:
        print('Opção inválida!\nTente novamente...')
        continue
 


