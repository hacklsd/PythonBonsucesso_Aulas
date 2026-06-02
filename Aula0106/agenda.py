def exibir_menu():
    print("\n--- AGENDA TELEFÔNICA ---")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Excluir contato")
    print("4. Sair")

def agenda():
    contatos = {}

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome: ").strip()
            numero = input("Digite o número: ").strip()
            contatos[nome] = numero
            print(f"Contato '{nome}' adicionado com sucesso!")

        elif opcao == '2':
            print("\n--- Lista de Contatos ---")
            if not contatos:
                print("Agenda vazia.")
            else:
                for nome, numero in contatos.items():
                    print(f"{nome}: {numero}")

        elif opcao == '3':
            nome = input("Digite o nome do contato que deseja excluir: ").strip()
            if nome in contatos:
                del contatos[nome]
                print(f"Contato '{nome}' excluído com sucesso!")
            else:
                print("Contato não encontrado.")

        elif opcao == '4':
            print("Encerrando agenda...")
            break
        else:
            print("Opção inválida, tente novamente.")

    agenda()
