    # Exemplo 1. IDENTAÇÃO:

temperatura = 30
if temperatura > 25:
    print('Hoje está calor...')

#############################################################################

    # Exemplo 3. TIPO DE VARIÁVEL: 

x = str(3)
print(type(x)) 

#############################################################################

    # Condicional simples: IF e ELSE: 

temperatura = int(input('Qual a temperatura na sua cidade hoje? '))
if temperatura <= 25:
    print('Hoje está frio...')
else:
    print('Hoje está calor ...')

#############################################################################

    # Desafio: Verifique se o número digitado pelo usuário é par ou ímpar, (dica: Use %2): 

numero = int(input('Digite um número: '))
if (numero %2 == 0):  # Aqui é como se estivesse dizendo: "Se o número digitado, for dividido por 2 e o resto for 0 (%2 == 0)... imprima PAR"
    print('PAR! ☺ ')
else: 
    print('ÍMPAR ☻ ')

#############################################################################
    
    # Desafio: Verifique se uma senha digitada é igual a "1234". Se sim, "login feito!"


senha_padrao = 1234
senha = int(input(' Digite sua senha'))
if senha == senha_padrao:
    print('Login feito...')
else:
    print('Senha incorreta...')

#############################################################################
    
    # Desafio: Verifique usuário e senha, depois autentique o acesso: 

usuario_padrao = "victor"
senha_padrao = 1234

usuario = input('Digite seu usuário: ')
senha = int(input('Digite sua senha: '))

if usuario == "victor" and senha == 1234: # Para comparar dois valores distintos na mesma linha, usa-se o AND, que é 
    print('Login concedido!')
else: 
    print('Login não autenticado! ')

#############################################################################


