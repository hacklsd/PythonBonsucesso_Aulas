# ESSE SCRIPT SERVE PARA AUTOMATIZAR O PROCESSO DE CRIAÇÃO DO DIRETÓRIO TEMPLATES, ASSIM COMO O ARQUIVO PRINCIPAL EM .HTML EM CADA SUBPASTA.

# O ARQUIVO AUTO_DIRETORIO.PY DEVE SER COLADO NA PASTA - APP - DO SEU PROJETO EM DJANGO. 

# PARA RODAR O SCRIPT, DENTRO DA PASTA APP, RODE O SEGUINTE COMANDO NO TERMINAL:

#   python auto_diretorio.py 
# ====================================================================================================================



# ==========================================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ==========================================================

# Importa a classe Path do módulo pathlib.
#
# O pathlib é a forma moderna (e recomendada) de trabalhar
# com arquivos e pastas em Python.
#
# Antes era comum usar:
# import os
#
# Hoje, Path torna o código mais legível e funciona em
# Windows, Linux e macOS sem precisar alterar barras (/ ou \).
from pathlib import Path


# ==========================================================
# ESTRUTURA DO PROJETO
# ==========================================================

# Toda a estrutura que desejamos criar ficará armazenada
# dentro deste dicionário.
#
# A ideia é simples:
#
# A chave principal representa a pasta principal.
#
# Exemplo:
# "templates"
#
# Dentro dela temos outro dicionário contendo:
#
# nome_da_pasta : lista_de_arquivos
#
# Isso facilita muito aumentar o projeto no futuro.

ESTRUTURA = {

    # Pasta principal
    "templates": {

        # Será criada:
        # templates/cadastro/
        "cadastro": [

            # Arquivos dentro da pasta cadastro
            "index.html",
        ],

        # Será criada:
        # templates/home/
        "home": [

            # Arquivo da pasta home
            "home.html",
        ],

        # Será criada:
        # templates/usuarios/
        "usuarios": [

            # Arquivo da pasta usuarios
            "index.html",
        ],
    }
}


# ==========================================================
# FUNÇÃO RESPONSÁVEL POR CRIAR A ESTRUTURA
# ==========================================================

def criar_estrutura(estrutura: dict) -> None:
    """
    Recebe um dicionário contendo uma estrutura de pastas
    e cria automaticamente todas elas.

    estrutura:
        dicionário contendo a organização do projeto.

    -> None

    Significa que esta função não retorna nenhum valor.
    Ela apenas executa ações.
    """

    # Percorre o primeiro nível do dicionário.
    #
    # Exemplo:
    #
    # pasta_principal = "templates"
    #
    # subpastas =
    # {
    #     "cadastro": [...],
    #     "home": [...],
    #     "usuarios": [...]
    # }

    for pasta_principal, subpastas in estrutura.items():

        # Converte o texto "templates"
        # em um objeto Path.
        #
        # Agora podemos usar métodos específicos para
        # manipular diretórios.

        pasta_principal = Path(pasta_principal)

        # Agora percorremos cada subpasta.
        #
        # Primeira repetição:
        #
        # subpasta = cadastro
        # arquivos = ["index.html"]

        for subpasta, arquivos in subpastas.items():

            # Junta os caminhos.
            #
            # Resultado:
            #
            # templates/cadastro
            #
            # O operador "/" foi sobrescrito pela classe Path.
            #
            # Não é uma divisão.
            #
            # Ele apenas concatena caminhos.

            caminho = pasta_principal / subpasta

            # Cria a pasta.
            #
            # parents=True
            #
            # Caso a pasta principal ainda não exista,
            # ela também será criada.
            #
            # exist_ok=True
            #
            # Caso a pasta já exista,
            # o programa NÃO gera erro.

            caminho.mkdir(
                parents=True,
                exist_ok=True
            )

            # Agora percorremos todos os arquivos
            # que pertencem àquela pasta.

            for arquivo in arquivos:

                # Junta:
                #
                # templates/cadastro
                #
                # com
                #
                # index.html
                #
                # Resultado:
                #
                # templates/cadastro/index.html

                caminho_arquivo = caminho / arquivo

                # Verifica se o arquivo já existe.

                if not caminho_arquivo.exists():

                    # Caso não exista,
                    # cria um arquivo vazio.

                    caminho_arquivo.touch()

                    # Mostra ao usuário
                    # que o arquivo foi criado.

                    print(f"[CRIADO] {caminho_arquivo}")

                else:

                    # Caso já exista,
                    # apenas informa.

                    print(f"[EXISTE] {caminho_arquivo}")


# ==========================================================
# PONTO DE ENTRADA DO PROGRAMA
# ==========================================================

# Esta condição é extremamente importante.
#
# Ela verifica:
#
# "Este arquivo está sendo executado diretamente?"
#
# Se SIM:
#
# executa o código abaixo.
#
# Se este arquivo for importado em outro programa,
# tudo abaixo será ignorado.

if __name__ == "__main__":

    # Imprime uma linha de separação.

    print("=" * 50)

    # Título do programa.

    print("CRIADOR DE ESTRUTURAS DE PROJETO")

    # Outra linha.

    print("=" * 50)

    # Chama a função.
    #
    # Passamos o dicionário ESTRUTURA como argumento.
    #
    # A função irá percorrer tudo
    # e criar pastas e arquivos.

    criar_estrutura(ESTRUTURA)

    # Mensagem final.

    print("\nEstrutura criada com sucesso!")