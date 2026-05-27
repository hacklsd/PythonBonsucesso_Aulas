usuarios = []
saldos = []
session = []
login_sucesso = False


def cadastrar(nome, cpf, senha):
    usuarios.append({"usuario": nome,"cpf": cpf,"senha": senha})
    saldos.append({"cpf": cpf,"saldo": 0.0})
    print(f"Usuário {nome} cadastrado com sucesso!")

def login(cpf, senha):
    global login_sucesso
    global session
    login_sucesso = False
    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["senha"] == senha:
            login_sucesso = True
            session = {"cpf": usuario["cpf"],"usuario": usuario["usuario"]}
            print(f'Acesso liberado! Bem-vindo {usuario["usuario"]}')
            return
    print("Usuário não cadastrado.")

def add_saldo(valor, cpf):
    for conta in saldos:
        if conta["cpf"] == cpf:
            conta["saldo"] += valor
            print(f"Saldo atual: {conta['saldo']}")
            return
    print("Conta de saldo não encontrada para este CPF.")

def saque(valor_saque, cpf):
    for conta in saldos:
        if conta["cpf"] == cpf:
            conta["saldo"] -= valor_saque
            print(f"Saldo atual: {conta['saldo']}")
            return

def trocar_senha(cpf, senha_atual):
    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["senha"] == senha_atual:
            usuario["senha"] = input("Nova senha: ")
            print("Senha alterada com sucesso!")
            return
    print("Dados inválidos.")

def sistema():
    global login_sucesso, session
    while True:
        if login_sucesso:
            print("\n1. Adicionar Saldo | 2. Saque  | 3. Trocar senha | 4. Logout")
            opcao = input("Escolha: ")

            match opcao:
                case "1":
                    print('=== ADICIONAR SALDO ===\n')
                    cpf = session["cpf"]
                    valor = float(input("Informe o valor do depósito: "))
                    add_saldo(valor, cpf)

                case "2":
                    print('=== SAQUE ===\n')
                    cpf = session["cpf"]
                    valor_saque = float(input("Informe o valor do saque: "))
                    saque(valor_saque, cpf)

                case "3":
                    print('=== TROCAR SENHA ===\n')
                    cpf = int(input("CPF: "))
                    senha_atual = int(input("Senha atual: "))
                    trocar_senha(cpf, senha_atual)

                case "4":
                    print("Voltando ao menu principal.")
                    login_sucesso = False
                    session = []

                case _:
                    print("Opção inválida.")

        else:
            print("\n1. Cadastrar | 2. Login | 3. Trocar Senha | 4. Sair")
            opcao = input("Escolha: ")

            match opcao:
                case "1":
                    print("=== TELA DE CADASTRO ===\n")
                    nome = input("INSIRA SEU NOME: ")
                    cpf = int(input("INSIRA SEU CPF: "))
                    senha = int(input("INSIRA SUA SENHA: "))

                    cadastrar(nome, cpf, senha)

                case "2":
                    print("=== LOGIN ===\n")
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