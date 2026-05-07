"""
   1.  Solução: concatenação de int e str, usando f" (FString):


nome = str(input('Insira seu nome: '))
idade = int(input('Insira sua idade: '))
ano = 2026 - idade

print(nome, ", você nasceu em ", ano)              # → uma forma de concatenar strings e inteiros
print(f"{nome}, você nasceu em {ano}")             # → concatenando com uso de FString (f") onde os ints, entram entre {}
print(f"{nome}, você nasceu em {2026 - idade}")    # → Usando f", pode-se realizar tbm, cálculos entre {}
"""
"""
   2.  Solução: revisando uso de if, else, e elif: 


idade = int(input('Digite sua idade: '))
if idade < 5:
    print('Bebê')
if idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 65: 
    print('Adulto')
elif idade < 80:
    print('Velho')
elif idade < 100:
    print('Múmia')
else:
    print('já morreu...')

"""
"""
    3. 

nota = float(input('Qual foi sua nota? '))

if nota < 7:
    print('C')
elif nota < 9:
    print('B')
elif nota < 11:
    print('A')
else:
    print('Nota inválida')
"""
"""
    4. Switch Case: 

print('Menu: \n 1- Cadastro de usuário \n 2. Cadastro de Senha \n 3. Ajuda ')

menu = int(input('Escolha a opção desejada (Insira número): '))


match menu:
    case 1:
        usuario = str(input('Insira nome de usuário: '))
    case 2: 
        senha = input('Digite uma senha de 4 dígitos: ')
    case 3: 
        print('Ajuda: ')

"""
"""
    • Função: 

def sparta():
    x = 300 
    print(x)

sparta()

def besta():
    besta = 666
    print(besta)

print(str('Menu de avatares: \n 1. Besta \n 2. Sparta '))
menu = int(input('Escolha um avatar (escolha 1 ou 2): '))
match menu:
    case 1:
        besta()
    case 2:
        sparta()
"""
"""
    • Escopo: em Python como “a área onde uma variável existe e pode ser usada”


        EXEMPLO 1: ESCOPO LOCAL, é um lugar fechado onde a variável existe, no exemplo, observemos a variável x:


def myfunc():
    x = 300                                 → Definida a variável x, dentro da função myfunc

myfunc()                                    → Chamando a função myfunc

print(x)                                    → Tentando imprimir a variável x 

>>> NameError: name 'x' is not defined      → Resultado de erro, pois a variável x está no escopo da função myfunc. 

""" 
"""

# EXEMPLO 2: Escopo Global, é qualquer espaço fora de uma função, onde uma variável tem seu valor atribuído; oberseve a variável x 

x = 200             # → Variável x, tem seu valor atribuído fora da função 

def myfunc():       # → Aqui cria-se a função myfunc
    global x        # → Com a ferramenta 'global' indicamos que estamos pegando a variável em escopo global, para dentro da função (myfunc)
    x = 300         # → Aqui a função myfunc atribui um novo valor à variável x 

myfunc()            # → Ao chamar a função, ela executa sua meta (nesse caso atribuir o valor de 300 à variável x)
print(x)            # → Aqui imprime a variável x, com seu novo valor atribuído pela função.

"""
"""
def myfunc():
    print('Executando a função \n')

    def myinnerfunc():
        print('Executando a função dentro da função \n')
        

    myinnerfunc()
myfunc()

# Resultado:
# >>> Executando a função 
#
#     Executando a função dentro da função
"""

    # ESCOPO NÃO LOCAL: 
x = "Escopo global"

def myfunc1():
  x = "função 1"
  def myfunc2():
      nonlocal x
      x = "alterado na função 2"
      print(x)

  myfunc2()
  print(x)    
myfunc1()
print(x)


