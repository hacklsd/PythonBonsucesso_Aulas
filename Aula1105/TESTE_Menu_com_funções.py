usuario = ""
senha = ""

def Cadastro():
    global usuario
    global senha
    usuario = input('Digite seu nome de usuário: ')
    senha = int(input('Digite sua senha: SOMENTE NÚMEROS: '))

def login():
    global loginusuario
    loginusuario = input('digite seu nome de usuário: ')
    if loginusuario == usuario:
        print("Usuário confirmado, continue...")
    global loginsenha
    loginsenha = int(input('Digite sua senha: SOMENTE NÚMEROS: '))
    if loginsenha == senha:
        print("Senha confirmada! Acesso Liberado! ")
    else: 
        print("Tente novamente! ")



def sair():
    print('Obrigado por usar nosso APP! ')



menu = '''
♥ BEM VINDO AO APP ♥

ESCOLHA UMA DAS OPÇÕES ABAIXO:

[1] CADASTRO
[2] LOGIN
[3] SAIR
'''

print(menu)

opcoes = int(input(""))


match opcoes:
    case 1:
        Cadastro()
    case 2: 
        login()
    case 3: 
        sair()

