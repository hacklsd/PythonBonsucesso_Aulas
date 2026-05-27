usuarios = []
saldo = []
session = []
login_sucesso = False                           

def cadastrar(nome, cpf, senha):    
    usuarios.append({"usuario": nome, "cpf": cpf, "senha": senha})
    saldo.append({"cpf": cpf, "saldo": 0.0})
    print(f"Usuário {nome} cadastrado com sucesso!")
    


def login(cpf, senha):  
   
    global login_sucesso
    login_sucesso = False
    for u in usuarios:
        if u["cpf"] == cpf and u["senha"] == senha:    
            login_sucesso = True
            global session
            session = {"cpf": u["cpf"], "usuario": u["usuario"]}
            print(f"Acesso liberado! Bem vindo {u["usuario"]}")   
            break

        print("Acesso Liberado!" if login_sucesso else "Usuário não cadastrado.")
        login_sucesso = False
        

def add_saldo(saldo, cpf):  
    for conta in saldo:
        if conta['cpf'] == cpf:
            conta['saldo'] += saldo
            return print(conta['saldo'])
    print('conta de saldo não encontrada para este CPF.')
     


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
        global session
        if login_sucesso:
            print("\n1. Adicionar Saldo | 2. Trocar Senha | 3. Logout")
            opcao = input("Escolha: ")

            match opcao:
                case "1":
                    if login_sucesso:
                        cpf = session["cpf"]
                        saldo = float(input('Informe o valor do depósito: '))
                        add_saldo(saldo, cpf)

                case "2":
                    trocar_senha()

                case "3":
                    print('Voltando ao menu principal. ')
                    login_sucesso = False
                    session = {}
                    
                case _:
                    print('Opção inválida. ')

        else:
            print("\n1. Cadastrar | 2. Login | 3. Trocar Senha: | 4. Sair")
            opcao = input("Escolha: ")

            match opcao:
                case "1":
                    print('=== TELA DE CADASTRO===\n')
                    nome = input('INSIRA SEU NOME: ')
                    cpf = int(input('INSIRA SEU CPF: '))
                    senha = int(input('INSIRA SUA SENHA: '))
                    cadastrar(nome, cpf, senha)

                case "2":
                    print("→ Tela de login: ")
                    cpf = int(input('CPF: '))                  
                    senha = int(input("Senha: "))
                    login(cpf, senha)

                case "3":
                    trocar_senha()

                case "4":
                    print("Saindo .... ")
                    break
sistema()
