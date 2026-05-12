def cadastro(n):
    print(f' {n}, Cadastro realizado com sucesso!!! ')
def login():
    print('Login realizado com sucesso!!! ')
def sair():
    print('Saindo, obrigado por usar nosso serviços! ')
def menu_principal():
    while True:
        print(menu)


menu = '''
→ BEM VINDO AO APP 

ESCOLHA UMA DAS OPÇÕES ABAIXO:

[1] CADASTRO
[2] LOGIN
[3] SAIR
'''

print(menu)

opcoes = int(input(""))


match opcoes:
    case 1:
        nome = input('Digite seu nome: ')
        cadastro(nome)

    case 2: 
        login = input("Digite o nome de usuário: ")
        login(login)
    case 3: 
        sair()        
    case _:
        print("Opção inválida! ")
    
menu_principal()
