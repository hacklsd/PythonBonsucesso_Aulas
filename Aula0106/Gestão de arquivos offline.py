# Importação de bibliotecas externas ("ferramentas" que o Python já tem prontas)
import json # Usada para ler e salvar arquivos no formato JSON (texto estruturado)
import os   # Usada para interagir com o sistema operacional (ex: checar se um arquivo existe)

# Variável constante (em maiúsculo por convenção) que define o nome do nosso banco de dados
ARQUIVO_DADOS = 'dados_arquivos.json'

def carregar_dados():
    """
    Função responsável por ler o arquivo JSON logo que o programa abre.
    Se o arquivo já existir, ele pega o texto e transforma em um Dicionário do Python.
    Se não existir (ex: primeira vez rodando), ele retorna um dicionário vazio {}.
    """
    # Checa se o arquivo já existe no computador
    if os.path.exists(ARQUIVO_DADOS):
        # Abre o arquivo em modo de leitura ('r' de read) com suporte a acentos (utf-8)
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f) # Converte o JSON em dados que o Python entende
    
    # Se o arquivo não existir, retorna um espaço vazio em branco na memória
    return {}

def salvar_dados(dados):
    """
    Sempre que houver um novo cadastro, essa função é chamada para reescrever
    o arquivo JSON no computador, garantindo que os dados não se percam.
    """
    # Abre (ou cria) o arquivo em modo de escrita ('w' de write)
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        # Pega a variável 'dados' e injeta no arquivo. 
        # ensure_ascii=False permite acentuação e indent=4 deixa o arquivo formatado e bonito.
        json.dump(dados, f, ensure_ascii=False, indent=4)

def cadastrar(dados):
    """
    Pede as informações para o usuário e adiciona no dicionário de dados.
    """
    print("\n--- Cadastro de Pasta ---")
    
    # input() aguarda o usuário digitar algo. strip() remove espaços vazios no início e no fim.
    nome = input("Nome da pasta/documento: ").strip()
    
    # Checa se a pasta já existe ignorando letras maiúsculas e minúsculas (.lower())
    if nome.lower() in [k.lower() for k in dados.keys()]:
        print("Aviso: Já existe uma pasta cadastrada com esse nome.")
        return # Interrompe o cadastro e volta para o menu
    
    coluna = input("Coluna (Arquivo): ").strip()
    gaveta = input("Linha (Gaveta): ").strip()
    
    # Cria uma nova entrada no dicionário. O 'nome' da pasta é a chave principal.
    # Dentro dessa chave, guardamos a coluna e a gaveta.
    dados[nome] = {"coluna": coluna, "gaveta": gaveta}
    
    # Chama a função de salvar para registrar a alteração no arquivo físico no computador
    salvar_dados(dados)
    print("Sucesso: Pasta cadastrada e salva!")

def pesquisar(dados):
    """
    Busca por um termo digitado pelo usuário dentro das pastas cadastradas.
    """
    print("\n--- Pesquisa de Pasta ---")
    termo = input("Digite o nome da pasta para buscar: ").strip().lower()
    
    # Variável de controle para sabermos se achamos algo ou não
    encontrado = False
    
    # Faz um loop por todos os itens cadastrados no nosso dicionário
    for nome, local in dados.items():
        # Verifica se o 'termo' digitado faz parte do 'nome' cadastrado
        if termo in nome.lower():
            print(f"> Encontrado: '{nome}' | Coluna (Arquivo): {local['coluna']} | Linha (Gaveta): {local['gaveta']}")
            encontrado = True # Marcamos que encontramos pelo menos um resultado
            
    # Se ao final do loop a variável continuar False, significa que não achou nada
    if not encontrado:
        print("Nenhuma pasta encontrada contendo esse termo.")

def exibir_salvos(dados):
    """
    Lista tudo que está armazenado atualmente na memória, em ordem alfabética.
    """
    print("\n--- Pastas Salvas ---")
    
    # Se o dicionário estiver vazio, o Python entende como Falso
    if not dados:
        print("O sistema ainda não possui pastas cadastradas.")
        return
    
    # Organiza os itens do dicionário em ordem alfabética pela chave (nome da pasta).
    # O .lower() garante que a ordem não seja afetada por letras maiúsculas/minúsculas.
    itens_ordenados = sorted(dados.items(), key=lambda item: item[0].lower())
    
    # Loop para imprimir cada item da nova lista ordenada, linha por linha
    for nome, local in itens_ordenados:
        print(f"- {nome}: Coluna {local['coluna']}, Linha {local['gaveta']}")

def main():
    """
    Função principal. É aqui que a mágica começa e a interação com o usuário acontece.
    """
    # Passo 1: Puxa os dados antigos do HD para a memória RAM (variável 'dados')
    dados = carregar_dados()
    
    # O 'while True' cria um laço de repetição infinito (Menu).
    # O programa só sairá desse laço se forçarmos a parada com o comando 'break' (Opção 4).
    while True:
        print("\n==============================")
        print("      GESTÃO DE ARQUIVOS        ")
        print("==============================")
        print("1. Cadastrar nova pasta")
        print("2. Pesquisar pasta")
        print("3. Exibir pastas salvas")
        print("4. Sair")
        print("==============================")
        
        # Pede para o usuário escolher o que fazer
        opcao = input("Escolha uma opção: ").strip()
        
        # O sistema de tomada de decisão (condicionais) baseado na escolha do usuário
        if opcao == '1':
            cadastrar(dados) # Leva para a função de cadastro
        elif opcao == '2':
            pesquisar(dados) # Leva para a função de busca
        elif opcao == '3':
            exibir_salvos(dados) # Leva para a função de exibir a lista
        elif opcao == '4':
            print("Encerrando o sistema...")
            break # Comando fundamental: quebra o 'while True' e finaliza o script
        else:
            # Caso o usuário digite '5', 'A' ou qualquer coisa não prevista
            print("Opção inválida. Digite um número de 1 a 4.")

# PONTO DE PARTIDA DO PROGRAMA
# Esta condição verifica se o script está sendo executado diretamente (e não importado por outro código).
# Se for verdadeiro, ele aciona a função main() logo acima, iniciando tudo.
if __name__ == "__main__":
    main()

