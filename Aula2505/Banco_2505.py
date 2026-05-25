usuarios = []
login_sucesso = False

def cadastrar():
    print("→ Tela de cadastro: ")
    nome = input("Escolha seu usuário: ")
    cpf = int(input('DIGITE SEU CPF: '))                                                #25/05 - Adicionado campo de CPF para preenchimento do cliente. (L7)
    senha = int(input("Escolha sua senha com até 4 dígitos: "))
    usuarios.append({"usuario": nome, "cpf": cpf, "senha": senha})
    print(f"Usuário {nome} cadastrado com sucesso!")


def login():
    print("→ Tela de login: ")
    cpf = int(input('CPF: '))                                                           #25/05 - Login passa a ser com CPF e SENHA. (L15)
    senha = int(input("Senha: "))
    global login_sucesso
    login_sucesso = False
    for u in usuarios:
        if u["cpf"] == cpf and u["senha"] == senha:                                     #25/05 - Login passa a ser com CPF e SENHA.(L20)
            print(f"Acesso liberado! Bem vindo {u["usuario"]}")                         #25/05 - Adicionado o nome do cliente, na mensagem de Acesso Liberado! (L21)
            login_sucesso = True
            break

        print("Acesso Liberado!" if login_sucesso else "Usuário não cadastrado.")
        login_sucesso = False
        


def trocar_senha():
    print("→ Tela de trocar a senha: ")
    cpf = int(input('CPF: '))
    senha_atual = int(input('Senha atual: '))
    for user in usuarios:
        if user["cpf"] == cpf and user["senha"] == senha_atual:
            user["senha"] = input('Nova senha: ')
            print("Senha alterada com sucesso! ")
            return
    print("Dados inválidos. ")
 

def sistema():
    while True:
        global login_sucesso
        if login_sucesso:
            print("\n1. Atendimento | 2. Trocar Senha | 3. Logout")
            opcao = input("Escolha: ")

            match opcao:
                case "1":
                    login()
                case "2":
                    trocar_senha()
                case "3":
                    print('Voltando ao menu principal. ')
                    login_sucesso = False
                   
                case _:
                    print('Opção inválida. ')

        else:
            print("\n1. Cadastrar | 2. Login | 3. Trocar Senha: | 4. Sair")
            opcao = input("Escolha: ")

            match opcao:
                case "1":
                    cadastrar()
                case "2":
                    login()
                case "3":
                    trocar_senha()
                case "4":
                    print("Saindo .... ")
                    break
sistema()
