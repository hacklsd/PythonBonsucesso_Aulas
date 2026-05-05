usuario_padrao = "victor"
senha_padrao = 1234

usuario = input('Digite seu usuário: ')
senha = int(input('Digite sua senha: '))

if usuario == "victor" and senha == 1234:
    print('Login concedido!')
else: 
    print('Login não autenticado! ')