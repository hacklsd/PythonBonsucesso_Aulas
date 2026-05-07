"""
• Revisando:

1.  Revisando: concatenação de int e str..
2.  Revisando: IF, ELSE, ELIF...
3.  Revisando: IF, ELSE, usando lista, e outras estruturas (IN)...

• Conteúdo novo: 

4.  Switch Case: É uma Ferramenta para criar menu de opções.
5.  Funções: É um trecho de código que só será executado quando chamado.
6.  Escopo: em Python como “a área onde uma variável existe e pode ser usada”


EXEMPLO 1: ESCOPO LOCAL, é um lugar fechado onde a variável existe, no exemplo, observemos a variável x:


def myfunc():
    x = 300                                 → Definida a variável x, dentro da função myfunc

myfunc()                                    → Chamando a função myfunc

print(x)                                    → Tentando imprimir a variável x 

>>> NameError: name 'x' is not defined      → Resultado de erro, pois a variável x está no escopo da função myfunc. 




EXEMPLO 2: Escopo Global, é qualquer espaço fora de uma função, onde uma variável tem seu valor atribuído; oberseve a variável x:

        
x = 200              → Variável x, tem seu valor atribuído fora da função 

def myfunc():        → Aqui cria-se a função myfunc
    global x         → Com a ferramenta 'global' indicamos que estamos pegando a variável em escopo global, para dentro da função (myfunc)
    x = 300          → Aqui a função myfunc atribui um novo valor à variável x 

myfunc()             → Ao chamar a função, ela executa sua meta (nesse caso atribuir o valor de 300 à variável x)
print(x)             → Aqui imprime a variável x, com seu novo valor atribuído pela função.

"""

