'''→  MÓDULOS:
    
    SÃO FUNÇÕES CRIADAS E SALVAS EM OUTROS ARQUIVOS,
    QUE PODEM SER IMPORTADOS E USADOS EM NOVAS CRIAÇÕES. 

    ALÉM DOS MÓDULOS QUE CRIAMOS, EXISTEM OS MÓDULOS
    NATIVOS DO PYTHON, AQUI VAMOS USAR UM MÓDULO PARTICULAR,
    CHAMADO meumodulo.py.

    PARA IMPORTAR MÓDULOS PARTICULARES, ELES PRECISAM ESTAR 
    NA MESMA PASTA DO CÓDIGO NOVO QUE ESTÁ SENDO CRIADO.
    
'''

import meumodulo        # LINHA DE IMPORTAÇÃO DE MÓDULO CRIADO.

meumodulo.somando(1)    # CHAMANDO A FUNÇÃO DO MÓDULO IMPORTADO.

# >>> saída: 2

''' Porque a função do meumodulo.py, 
    é somar o argumento por ele mesmo; 
    nesse caso, o 1 entre parênteses.

meumodulo.py

def somando(n):
    print(n + n)

'''
