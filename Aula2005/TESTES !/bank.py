import funcoes_bank
login_sucesso = False

def sistema():

    global login_sucesso

    while True:

        if login_sucesso:

            print("\n=== ÁREA LOGADA ===")
            print("1. Atendimento")
            print("2. Trocar senha")
            print("3. Logout")

            opcao = input("Escolha: ")

            match opcao:

                case "1":
                    print("Atendimento iniciado...")
                    funcoes_bank.atendimento()

                case "2":
                    funcoes_bank.trocar_senha()

                case "3":
                    print("Logout realizado.")
                    login_sucesso = False

                case _:
                    print("Opção inválida.")

        else:

            print("\n=== MENU PRINCIPAL ===")
            print("1. Cadastrar")
            print("2. Login")
            print("3. Trocar senha")
            print("4. Sair")

            opcao = input("Escolha: ")

            match opcao:

                case "1":
                    funcoes_bank.cadastrar()

                case "2":
                    funcoes_bank.login()

                case "3":
                    funcoes_bank.trocar_senha()

                case "4":
                    print("Saindo...")
                    break

                case _:
                    print("Opção inválida.")


sistema() 