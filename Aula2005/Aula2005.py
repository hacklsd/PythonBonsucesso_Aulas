'''→  MÓDULOS:
    
    SÃO FUNÇÕES CRIADAS E SALVAS EM OUTROS ARQUIVOS,
    QUE PODEM SER IMPORTADOS E USADOS EM NOVAS CRIAÇÕES. 

    ALÉM DOS MÓDULOS QUE CRIAMOS, EXISTEM OS MÓDULOS
    INTEGRADOS DO PYTHON, AQUI VAMOS USAR UM MÓDULO PARTICULAR,
    CHAMADO meumodulo.py.

    PARA IMPORTAR MÓDULOS PARTICULARES, ELES PRECISAM ESTAR 
    NA MESMA PASTA DO CÓDIGO NOVO QUE ESTÁ SENDO CRIADO.
    
'''
import platform             # MÓDULO INTEGRADO DO PYTHON.
import meumodulo            # LINHA DE IMPORTAÇÃO DE MÓDULO CRIADO.


x = meumodulo.somando(1)    # CHAMANDO A FUNÇÃO DO MÓDULO IMPORTADO.
# x = 1 + 1 → Traduzindo a linha acima, para a função .somando(1), do módulo meumodulo.py        
print(x)

# >>> saída: 2

''' Porque a função do meumodulo.py (que é substituir o argumento n, e retornar o valor da soma dela por ele mesmo), 
    é somar o argumento por ele mesmo; 
    nesse caso, o 1 entre parênteses.

meumodulo.py

def somando(n):
    return (n + n)

'''

a = meumodulo.person1["nome"]
print(a)

x = platform.system()
print(x)
y = platform.release()
print(y)
z = platform.version()
print(z)
