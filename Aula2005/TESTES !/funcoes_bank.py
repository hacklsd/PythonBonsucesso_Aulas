usuarios = []

def cadastrar():
    print("\n→ Tela de cadastro")

    nome = input("Escolha seu usuário: ").strip()
    senha = input("Escolha sua senha: ").strip()

    # Verifica usuário repetido
    for user in usuarios:
        if user["usuario"] == nome:
            print("Usuário já existe.")
            return

    usuarios.append({
        "usuario": nome,
        "senha": senha
    })

    print("Cadastro realizado com sucesso!")


def login():
    global login_sucesso

    print("\n→ Tela de login")

    nome = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    for user in usuarios:

        if user["usuario"] == nome and user["senha"] == senha:
            print("Login realizado com sucesso!")
            login_sucesso = True
            return

    print("Usuário ou senha inválidos.")
    login_sucesso = False


def trocar_senha():

    print("\n→ Trocar senha")

    nome = input("Usuário: ").strip()
    senha_atual = input("Senha atual: ").strip()

    for user in usuarios:

        if user["usuario"] == nome and user["senha"] == senha_atual:

            nova_senha = input("Nova senha: ").strip()

            user["senha"] = nova_senha

            print("Senha alterada com sucesso!")
            return

    print("Dados inválidos.")

def atendimento():
    print('\nATENDIMENTO:')
    print('-' * 12)
    print('1. SALDO')
    print('2. EXTRATO')
    print('3. PIX')
    print('4. VOLTAR')
    print('-' * 12)

    opcao = ""

    match opcao:
        case "1":
            print('SEU SALDO É: R$ 999.999.999')
            #saldo()

        case "2":
            print('EXTRATO: ')
            #extrato()
        case "3":
            print('ÁREA PIX:')
            #pix()
        case "4":
            print('...VOLTANDO AO MENU PRINCIPAL...')
 
        case "_":
            print('OPÇÃO INVÁLIDA!')
        

atendimento()


