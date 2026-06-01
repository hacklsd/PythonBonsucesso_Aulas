# ==============================================================================
# IMPORTAÇÕES BÁSICAS (Bibliotecas padrão do Python que vêm instaladas)
# ==============================================================================
import os          # Permite interagir com o Sistema Operacional (ex: limpar tela).
import sys         # Permite interagir com o interpretador Python (ex: forçar saída do terminal).
import time        # Usado para pausas e medição de tempo (ex: animações e delays).
import urllib.parse # Usado para codificar textos para formato de URL (URL Encoding).
from datetime import datetime # Usado para capturar a data e hora atual do sistema.

# ==============================================================================
# IMPORTAÇÕES EXTERNAS (Bibliotecas instaladas via pip)
# ==============================================================================
import phonenumbers # Motor do Google para validação e extração de metadados de telefones.
from phonenumbers import carrier, geocoder, timezone # Submódulos específicos de metadados.
from colorama import Fore, Style, init # Biblioteca para colorir o texto no terminal.

# Inicializa o Colorama. O 'autoreset=True' garante que a cor volte ao padrão 
# automaticamente após cada 'print', evitando que o terminal inteiro fique de uma cor só.
init(autoreset=True)

class LSDOsint:
    def __init__(self):
        # O método __init__ é o construtor da classe. Ele é executado automaticamente 
        # sempre que "instanciamos" a classe (criamos o objeto app = LSDOsint()).
        # Aqui, armazenamos os textos longos (banners) como atributos da classe para manter o código limpo.
        self.banner_texto = f"""
{Fore.CYAN}██████╗ ██████╗ ██╗   ██╗██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝
██████╔╝██████╔╝ ╚████╔╝ ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  
██╔═══╝ ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  
██║     ██║  ██║   ██║   ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
        {Fore.RED}██╗   ██╗███████╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗
        {Fore.RED}██║   ██║██╔════╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║
        {Fore.RED}██║   ██║█████╗  ██████╔╝███████╗██║██║   ██║██╔██╗ ██║
        {Fore.RED}╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║██║   ██║██║╚██╗██║
         {Fore.RED}╚████╔╝ ███████╗██║  ██║███████║██║╚██████╔╝██║ ╚████║
          {Fore.RED}╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
{Fore.GREEN}             [+]    by Large System Decoder        [+]
        """

        self.arte_maritima = f"""
            {Fore.CYAN}^^                    {Fore.YELLOW}@@@@@@@@@
       ^^        ^^             {Fore.YELLOW}@@@@@@@@@@@@@@@
                               {Fore.YELLOW}@@@@@@@@@@@@@@@@@@              {Fore.CYAN}^^
                              {Fore.YELLOW}@@@@@@@@@@@@@@@@████
{Fore.BLUE}~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~?? ~~~
~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~        ~~     ~~ ~
  ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~      ~~~    ~ ~~~  ~ ~~ 
  ~  ~~     ~         ~      ~~~~~~  ~~ ~~~        ~~ ~ ~~  ~~ ~ 
~  ~       ~ ~      ~            ~~ ~~~~~~  ~      ~~  ~               ~~
      ~              ~        ~      ~      ~~   ~              ~
"""

    def clear_screen(self):
        # Forma cross-platform (funciona em qualquer S.O) para limpar a tela.
        # Se os.name for 'nt' (Windows), ele roda o comando 'cls'.
        # Caso contrário (Linux/Mac), ele roda 'clear'.
        os.system('cls' if os.name == 'nt' else 'clear')

    def animate_text(self, text, delay=0.005, color=Fore.WHITE):
        # Cria um efeito visual de máquina de escrever.
        for char in text:
            sys.stdout.write(color + char) # write() imprime sem quebrar a linha no final.
            sys.stdout.flush()             # flush() força o terminal a exibir o caractere imediatamente.
            time.sleep(delay)              # Pausa minúscula entre cada letra.
        print() # Uma quebra de linha ao final do texto completo.

    def loading_animation(self, duration=1.2):
        # Animação de carregamento simulada para melhor experiência do usuário.
        spinner = ['|', '/', '-', '\\']
        end_time = time.time() + duration # Calcula o momento exato em que a animação deve parar.
        idx = 0
        sys.stdout.write(f"{Fore.YELLOW}[*] Cruzando dados de redes e mensageiros... ")
        
        # Enquanto o tempo atual for menor que o tempo de parada...
        while time.time() < end_time:
            # Imprime o símbolo atual do spinner baseado no resto da divisão (loop infinito na lista).
            sys.stdout.write(spinner[idx % len(spinner)])
            sys.stdout.flush()
            time.sleep(0.08)
            sys.stdout.write('\b') # '\b' é o backspace. Ele apaga o último símbolo para colocar o próximo por cima.
            idx += 1
        print(f"{Fore.GREEN}Concluído!")

    def validate_and_parse(self, phone_input):
        # Função para garantir que a entrada do usuário não vá quebrar o código (Tolerância a falhas).
        try:
            # Se o usuário esquecer o "+" (código do país), o script tenta consertar sozinho.
            if not phone_input.startswith('+'):
                # Presume que números de 10 a 11 dígitos sem "+" são números locais do Brasil.
                if len(phone_input) >= 10 and len(phone_input) <= 11:
                    phone_input = "+55" + phone_input
                else:
                    raise ValueError() # Força um erro se for um número absurdamente pequeno/grande.
            
            # O parse converte a string em um objeto PhoneNumber do Google.
            parsed_num = phonenumbers.parse(phone_input, None)
            
            # Verifica matematicamente se o número é possível existir nas regras daquele país.
            if not phonenumbers.is_valid_number(parsed_num):
                return None
            return parsed_num
        except Exception:
            # Se o usuário digitar letras ou lixo, o código cai aqui silenciosamente sem crashear.
            return None

    def save_results_to_file(self, international_format, national_format, country_code, regiao, operadora, tipo_str, fuso_horario, raw_digits, pure_national):
        # Pega o diretório onde o script está sendo executado
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Cria a pasta 'logs' se ela não existir
        logs_dir = os.path.join(script_dir, 'logs')
        os.makedirs(logs_dir, exist_ok=True)
        
        # Pega a data e hora atual no formato AnoMesDia_HoraMinutoSegundo para criar um nome de arquivo único.
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"osint_results_{pure_national}_{timestamp}.txt"
        filepath = os.path.join(logs_dir, filename)
        
        try:
            # O 'with open' é um Context Manager. Ele abre o arquivo em modo escrita ('w') 
            # e garante que o arquivo será fechado corretamente mesmo que ocorra um erro no meio do processo.
            with open(filepath, 'w', encoding='utf-8') as f:
                # Escrevemos os dados da mesma forma que aparecem na tela, mas sem as cores.
                f.write("=" * 60 + "\n")
                f.write("RELATÓRIO DE INTELIGÊNCIA OSINT - LSD_OSINT\n")
                f.write("=" * 60 + "\n")
                f.write(f"Data/Hora da Consulta: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
                
                f.write("METADADOS DA LINHA\n")
                f.write("-" * 60 + "\n")
                f.write(f"Formato Internacional : {international_format}\n")
                f.write(f"Formato Nacional      : {national_format}\n")
                f.write(f"Código do País (CC)   : +{country_code}\n")
                f.write(f"Localização Estimada  : {regiao if regiao else 'Não identificada'}\n")
                f.write(f"Operadora Original    : {operadora if operadora else 'Desconhecida/Portada'}\n")
                f.write(f"Tipo de Linha         : {tipo_str}\n")
                f.write(f"Fuso Horário          : {', '.join(fuso_horario)}\n\n")
                
                f.write("ANÁLISE DE MENSAGEIROS\n")
                f.write("-" * 60 + "\n")
                f.write(f"[WhatsApp Pessoal]\n")
                f.write(f"Link Direto: https://api.whatsapp.com/send?phone={raw_digits}\n")
                f.write(f"Detalhes   : Se ativo, abre a conversa e expõe a foto/recado pública.\n\n")
                
                f.write(f"[WhatsApp Business]\n")
                f.write(f"Link Direto: https://wa.me/{raw_digits}\n")
                f.write(f"Detalhes   : Se for conta comercial, pode expor catálogo de produtos, endereço e e-mail corporativo.\n\n")
                
                f.write(f"[Telegram Messenger]\n")
                f.write(f"Link Direto: https://t.me/+{raw_digits}\n")
                f.write(f"Detalhes   : Força o disparo do protocolo t.me. Se o usuário permitir busca por telefone, o perfil abrirá.\n\n")
                
                f.write(f"[Signal Messenger]\n")
                f.write(f"Link Direto: sgnl://signal.me/#p/+{raw_digits}\n")
                f.write(f"Detalhes   : Protocolo interno 'sgnl://'. Requer aplicativo Signal instalado no sistema.\n\n")
                
                f.write(f"[Viber Messenger]\n")
                f.write(f"Link Direto: viber://chat?number=%2B{raw_digits}\n")
                f.write(f"Detalhes   : Link de protocolo para o ecossistema Viber.\n\n")
                
                f.write("PEGADA DIGITAL & SPAM\n")
                f.write("-" * 60 + "\n")
                
                # urllib.parse.quote converte caracteres especiais em formato URL.
                # Exemplo: um espaço " " vira "%20", um "+" vira "%2B". Isso evita links quebrados no navegador.
                encoded_num = urllib.parse.quote(international_format)
                encoded_national = urllib.parse.quote(pure_national)
                
                f.write(f"Google Dork (Fidelidade): https://www.google.com/search?q=%22{encoded_num}%22+OR+%22{encoded_national}%22\n")
                f.write(f"Identificador Spam (Tellows): https://www.tellows.com.br/num/{encoded_national}\n")
                f.write(f"Quem Pertence (Base Pública): https://www.quempertence.com.br/Buscar?q={encoded_national}\n")
                f.write("=" * 60 + "\n")
            
            print(f"{Fore.GREEN}[+] Resultados salvos em: {filepath}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[ERRO] Falha ao salvar arquivo: {e}")
            return False

    def process_phone(self, phone_string):
        # Chama a função de validação. Se retornar None, o número é inválido.
        parsed = self.validate_and_parse(phone_string)
        if not parsed:
            print(f"\n{Fore.RED}[ERRO] Número inválido ou formato incorreto. Use: +5511999999999")
            return

        print()
        self.loading_animation(1.5)

        # O bloco 'try' envolve a extração de dados porque APIs externas (como a do geocoder) 
        # podem falhar se a base de dados estiver corrompida ou o número for muito anômalo.
        try:
            # Formatações úteis do número.
            international_format = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            national_format = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
            pure_national = str(parsed.national_number)
            raw_digits = f"{parsed.country_code}{pure_national}" 
            
            # Consultas no banco de dados local do phonenumbers (Engine do Android/Google).
            regiao = geocoder.description_for_number(parsed, "pt-br")
            operadora = carrier.name_for_number(parsed, "pt-br")
            fuso_horario = timezone.time_zones_for_number(parsed)
            tipo_linha = phonenumbers.number_type(parsed)

            # O motor do Google retorna um código numérico para o tipo de linha. 
            # Este dicionário mapeia o número retornado para um texto legível por humanos.
            tipos = {
                0: "Fixo (Fixed Line)", 1: "Móvel (Mobile)", 2: "Fixo ou Móvel",
                3: "Toll-Free (Gratuito)", 4: "Premium Rate", 5: "Shared Cost",
                6: "VoIP", 7: "Personal Number", 8: "Pager", 9: "Universal Access"
            }
            # O .get() tenta achar a chave. Se não achar, retorna "Desconhecido" por segurança.
            tipo_str = tipos.get(tipo_linha, "Desconhecido")

            # ==============================================================================
            # BLOCOS DE EXIBIÇÃO VISUAL (Prints na tela do usuário)
            # ==============================================================================
            
            # Painel de Metadados Gerais
            print(f"\n{Fore.GREEN}=================== METADADOS DA LINHA ===================")
            print(f"{Fore.YELLOW}Formato Internacional : {Fore.WHITE}{international_format}")
            print(f"{Fore.YELLOW}Formato Nacional      : {Fore.WHITE}{national_format}")
            print(f"{Fore.YELLOW}Código do País (CC)   : {Fore.WHITE}+{parsed.country_code}")
            print(f"{Fore.YELLOW}Localização Estimada  : {Fore.WHITE}{regiao if regiao else 'Não identificada'}")
            print(f"{Fore.YELLOW}Operadora Original    : {Fore.WHITE}{operadora if operadora else 'Desconhecida/Portada'}")
            print(f"{Fore.YELLOW}Tipo de Linha         : {Fore.WHITE}{tipo_str}")
            print(f"{Fore.YELLOW}Fuso Horário          : {Fore.WHITE}{', '.join(fuso_horario)}")
            
            # Painel de Deep Links para Mensageiros
            print(f"\n{Fore.CYAN}================ ANÁLISE DE MENSAGEIROS ================")
            print(f"{Fore.WHITE}Use os links gerados para forçar a resolução do perfil no app/web.")
            print("-" * 56)
            
            print(f"{Fore.GREEN}[WhatsApp Pessoal]{Fore.WHITE}")
            print(f" └─ Link Direto: {Fore.LIGHTBLUE_EX}https://api.whatsapp.com/send?phone={raw_digits}")
            print(f" └─ Detalhes   : Se ativo, abre a conversa e expõe a foto/recado pública.")
            print()
            print(f"{Fore.GREEN}[WhatsApp Business]{Fore.WHITE}")
            print(f" └─ Link Direto: {Fore.LIGHTBLUE_EX}https://wa.me/{raw_digits}")
            print(f" └─ Detalhes   : Se for conta comercial, pode expor catálogo de produtos, endereço e e-mail corporativo.")
            print()
            print(f"{Fore.GREEN}[Telegram Messenger]{Fore.WHITE}")
            print(f" └─ Link Direto: {Fore.LIGHTBLUE_EX}https://t.me/+{raw_digits}")
            print(f" └─ Detalhes   : Força o disparo do protocolo t.me. Se o usuário permitir busca por telefone, o perfil abrirá.")
            print()
            print(f"{Fore.GREEN}[Signal Messenger]{Fore.WHITE}")
            print(f" └─ Link Direto: {Fore.LIGHTBLUE_EX}sgnl://signal.me/#p/+{raw_digits}")
            print(f" └─ Detalhes   : Protocolo interno 'sgnl://'. Requer aplicativo Signal instalado no sistema.")
            print()
            print(f"{Fore.GREEN}[Viber Messenger]{Fore.WHITE}")
            print(f" └─ Link Direto: {Fore.LIGHTBLUE_EX}viber://chat?number=%2B{raw_digits}")
            print(f" └─ Detalhes   : Link de protocolo para o ecossistema Viber.")

            # Motores de Busca e Inteligência Auxiliar
            print(f"\n{Fore.MAGENTA}================ PEGADA DIGITAL & SPAM ===================")
            
            # Codificamos novamente os textos aqui para montar as URLs de busca de forma segura.
            encoded_num = urllib.parse.quote(international_format)
            encoded_national = urllib.parse.quote(pure_national)
            
            print(f"{Fore.YELLOW}Google Dork (Fidelidade): {Fore.LIGHTBLUE_EX}https://www.google.com/search?q=%22{encoded_num}%22+OR+%22{encoded_national}%22")
            print(f"{Fore.YELLOW}Identificador Spam (Tellows): {Fore.LIGHTBLUE_EX}https://www.tellows.com.br/num/{encoded_national}")
            print(f"{Fore.YELLOW}Quem Pertence (Base Pública): {Fore.LIGHTBLUE_EX}https://www.quempertence.com.br/Buscar?q={encoded_national}")
            print(f"{Fore.GREEN}========================================================\n")

            # Após mostrar na tela, chamamos a função que grava o arquivo.txt.
            self.save_results_to_file(
                international_format, national_format, parsed.country_code,
                regiao, operadora, tipo_str, fuso_horario, raw_digits, pure_national
            )

        except Exception as e:
            # Qualquer erro imprevisto nas linhas acima cairá aqui, impedindo que o script feche na cara do usuário.
            print(f"{Fore.RED}[ERRO CRÍTICO] Falha ao processar inteligência do número: {e}")

    def menu(self):
        # Um 'while True' cria um loop infinito. Isso significa que, após fazer uma pesquisa, 
        # o usuário voltará para o menu em vez de precisar abrir o programa de novo.
        while True:
            self.clear_screen()
            print(self.banner_texto)
            print(self.arte_maritima)
            print(f"{Fore.WHITE}[ 1 ] Consultar Inteligência do Número")
            print(f"{Fore.WHITE}[ 2 ] Termos de Uso e Compliance Ético")
            print(f"{Fore.WHITE}[ 3 ] Sair da Suite")
            print(f"{Fore.BLUE}-" * 70)
            
            # Pede a entrada do usuário. O .strip() remove espaços vazios acidentais antes e depois do texto digitado.
            opcao = input(f"{Fore.CYAN}Defina sua ação: {Fore.WHITE}").strip()

            if opcao == '1':
                print(f"\n{Fore.YELLOW}Exemplo de entrada aceita: +5511999999999 ou apenas o DDD+Número (BR)")
                alvo = input(f"{Fore.CYAN}Digite o número alvo: {Fore.WHITE}").strip()
                if alvo:
                    self.process_phone(alvo)
                else:
                    print(f"{Fore.RED}[!] Entrada inválida.")
                input(f"\nPressione {Fore.YELLOW}ENTER{Fore.WHITE} para retornar ao menu...")
            
            elif opcao == '2':
                self.clear_screen()
                print(f"\n{Fore.GREEN}================ NOTA DE COMPLIANCE ÉTICO ================")
                self.animate_text(
                    "Esta ferramenta opera sob estrito cumprimento das leis de privacidade.\n"
                    "A geração de Deep Links baseia-se nos protocolos oficiais de roteamento\n"
                    "das próprias empresas de tecnologia. O cruzamento com motores de busca\n"
                    "utiliza indexações puramente públicas, resguardando o legítimo interesse\n"
                    "investigativo e a conformidade legal.", delay=0.005, color=Fore.WHITE
                )
                print(f"{Fore.GREEN}========================================================\n")
                input(f"Pressione {Fore.YELLOW}ENTER{Fore.WHITE} para voltar...")
            
            elif opcao == '3':
                # Opção de saída. O comando 'break' destrói o loop 'while True', encerrando o script naturalmente.
                print(f"\n{Fore.RED}[*] Fechando painel LSD_OSINT de forma limpa...")
                time.sleep(1)
                break
            else:
                # Se o usuário digitar algo diferente de 1, 2 ou 3.
                print(f"\n{Fore.RED}[!] Opção inexistente.")
                time.sleep(1)

# ==============================================================================
# PONTO DE ENTRADA DO SCRIPT
# ==============================================================================
# Esta condicional verifica se o arquivo está sendo executado diretamente (como um programa) 
# ou se está sendo importado como uma biblioteca dentro de outro projeto.
if __name__ == "__main__":
    try:
        # Instancia e roda a aplicação.
        app = LSDOsint()
        app.menu()
    except KeyboardInterrupt:
        # Se o usuário apertar Ctrl+C (o atalho padrão para matar processos no terminal),
        # em vez de cuspir uma mensagem de erro feia de sistema (Traceback), ele sai elegante.
        print(f"\n\n{Fore.RED}[!] Operação abortada via Ctrl+C. Desconectando.")
        sys.exit(0) # O '0' significa que o programa terminou com sucesso/sem erros catastróficos.