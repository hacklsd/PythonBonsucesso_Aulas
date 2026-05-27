usuarios = []
saldos = {}
session = {}
login_sucesso = False


def cadastrar(nome, cpf, senha):
    usuarios.append({
        "usuario": nome, "cpf": cpf, "senha": senha})
    saldos[cpf] = 0.0
    print(f"Usuário {nome} cadastrado com sucesso!")


def login(cpf, senha):
    global login_sucesso
    global session
    login_sucesso = False
    for u in usuarios:
        if u["cpf"] == cpf and u["senha"] == senha:
            login_sucesso = True
            session = {
                "cpf": u["cpf"],
                "usuario": u["usuario"]
            }
            print(f'Acesso liberado! Bem-vindo {u["usuario"]}')
            return

    print("Usuário não cadastrado.")


def add_saldo(valor, cpf):

    saldos[cpf] += valor
    print(f"R$ {valor} adicionado com sucesso!")


def trocar_senha():
    cpf = int(input("CPF: "))
    senha_atual = int(input("Senha atual: "))
    for user in usuarios:
        if user["cpf"] == cpf and user["senha"] == senha_atual:
            nova_senha = int(input("Nova senha: "))
            user["senha"] = nova_senha
            print("Senha alterada com sucesso!")
            return

    print("Dados inválidos.")


def sistema():
    global login_sucesso
    global session

    while True:

        if login_sucesso:

            print("\n1. Adicionar Saldo | 2. Trocar Senha | 3. Logout")
            opcao = input("Escolha: ")

            match opcao:

                case "1":
                    valor = float(input("Informe o valor do depósito: "))
                    cpf = session["cpf"]

                    add_saldo(valor, cpf)

                case "2":
                    trocar_senha()

                case "3":
                    print("Voltando ao menu principal.")

                    login_sucesso = False
                    session = {}

                case _:
                    print("Opção inválida.")

        else:

            print("\n1. Cadastrar | 2. Login | 3. Trocar Senha | 4. Sair")
            opcao = input("Escolha: ")

            match opcao:

                case "1":
                    print("=== TELA DE CADASTRO ===\n")

                    nome = input("Insira seu nome: ")
                    cpf = int(input("Insira seu CPF: "))
                    senha = int(input("Insira sua senha: "))

                    cadastrar(nome, cpf, senha)

                case "2":
                    print("→ Tela de login")

                    cpf = int(input("CPF: "))
                    senha = int(input("Senha: "))

                    login(cpf, senha)

                case "3":
                    trocar_senha()

                case "4":
                    print("Saindo...")
                    break

                case _:
                    print("Opção inválida.")


sistema()