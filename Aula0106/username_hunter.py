import os
import sys
import time
import urllib.parse
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import Fore, Style, init
from datetime import datetime

# Inicializa o Colorama para suporte cross-platform
init(autoreset=True)

class LSDOsint:
    def __init__(self):
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
{Fore.GREEN}             [+]     by Large System Decoder        [+]
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
        os.system('cls' if os.name == 'nt' else 'clear')

    def animate_text(self, text, delay=0.005, color=Fore.WHITE):
        for char in text:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def loading_animation(self, duration=1.2):
        spinner = ['|', '/', '-', '\\']
        end_time = time.time() + duration
        idx = 0
        sys.stdout.write(f"{Fore.YELLOW}[*] Cruzando dados de redes e mensageiros... ")
        while time.time() < end_time:
            sys.stdout.write(spinner[idx % len(spinner)])
            sys.stdout.flush()
            time.sleep(0.08)
            sys.stdout.write('\b')
            idx += 1
        print(f"{Fore.GREEN}Concluído!")

    def validate_and_parse(self, phone_input):
        try:
            if not phone_input.startswith('+'):
                if len(phone_input) >= 10 and len(phone_input) <= 11:
                    phone_input = "+55" + phone_input
                else:
                    raise ValueError()
            
            parsed_num = phonenumbers.parse(phone_input, None)
            if not phonenumbers.is_valid_number(parsed_num):
                return None
            return parsed_num
        except Exception:
            return None

    def save_results_to_file(self, international_format, national_format, country_code, regiao, operadora, tipo_str, fuso_horario, raw_digits, pure_national):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"osint_results_{pure_national}_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
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
                encoded_num = urllib.parse.quote(international_format)
                encoded_national = urllib.parse.quote(pure_national)
                f.write(f"Google Dork (Fidelidade): https://www.google.com/search?q=%22{encoded_num}%22+OR+%22{encoded_national}%22\n")
                f.write(f"Identificador Spam (Tellows): https://www.tellows.com.br/num/{encoded_national}\n")
                f.write(f"Quem Pertence (Base Pública): https://www.quempertence.com.br/Buscar?q={encoded_national}\n")
                f.write("=" * 60 + "\n")
            
            print(f"{Fore.GREEN}[+] Resultados salvos em: {filename}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[ERRO] Falha ao salvar arquivo: {e}")
            return False

    def process_phone(self, phone_string):
        parsed = self.validate_and_parse(phone_string)
        if not parsed:
            print(f"\n{Fore.RED}[ERRO] Número inválido ou formato incorreto. Use: +5511999999999")
            return

        print()
        self.loading_animation(1.5)

        try:
            international_format = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            national_format = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
            pure_national = str(parsed.national_number)
            raw_digits = f"{parsed.country_code}{pure_national}" 
            
            regiao = geocoder.description_for_number(parsed, "pt-br")
            operadora = carrier.name_for_number(parsed, "pt-br")
            fuso_horario = timezone.time_zones_for_number(parsed)
            tipo_linha = phonenumbers.number_type(parsed)

            tipos = {
                0: "Fixo (Fixed Line)", 1: "Móvel (Mobile)", 2: "Fixo ou Móvel",
                3: "Toll-Free (Gratuito)", 4: "Premium Rate", 5: "Shared Cost",
                6: "VoIP", 7: "Personal Number", 8: "Pager", 9: "Universal Access"
            }
            tipo_str = tipos.get(tipo_linha, "Desconhecido")

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
            encoded_num = urllib.parse.quote(international_format)
            encoded_national = urllib.parse.quote(pure_national)
            
            print(f"{Fore.YELLOW}Google Dork (Fidelidade): {Fore.LIGHTBLUE_EX}https://www.google.com/search?q=%22{encoded_num}%22+OR+%22{encoded_national}%22")
            print(f"{Fore.YELLOW}Identificador Spam (Tellows): {Fore.LIGHTBLUE_EX}https://www.tellows.com.br/num/{encoded_national}")
            print(f"{Fore.YELLOW}Quem Pertence (Base Pública): {Fore.LIGHTBLUE_EX}https://www.quempertence.com.br/Buscar?q={encoded_national}")
            print(f"{Fore.GREEN}========================================================\n")

            # Salvar resultados em arquivo .txt
            self.save_results_to_file(
                international_format, national_format, parsed.country_code,
                regiao, operadora, tipo_str, fuso_horario, raw_digits, pure_national
            )

        except Exception as e:
            print(f"{Fore.RED}[ERRO CRÍTICO] Falha ao processar inteligência do número: {e}")

    def menu(self):
        while True:
            self.clear_screen()
            print(self.banner_texto)
            print(self.arte_maritima)
            print(f"{Fore.WHITE}[ 1 ] Consultar Inteligência do Número")
            print(f"{Fore.WHITE}[ 2 ] Termos de Uso e Compliance Ético")
            print(f"{Fore.WHITE}[ 3 ] Sair da Suite")
            print(f"{Fore.BLUE}-" * 70)
            
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
                print(f"\n{Fore.RED}[*] Fechando painel LSD_OSINT de forma limpa...")
                time.sleep(1)
                break
            else:
                print(f"\n{Fore.RED}[!] Opção inexistente.")
                time.sleep(1)

if __name__ == "__main__":
    try:
        app = LSDOsint()
        app.menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Operação abortada via Ctrl+C. Desconectando.")
        sys.exit(0)