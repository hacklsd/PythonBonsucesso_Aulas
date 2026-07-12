Saber automatizar o Terminal é uma das habilidades que mais aumenta sua produtividade com Python. É a base para criar instaladores, ferramentas DevOps, deploys, automações de servidores, scripts para Django e até bots.



Módulo - Automação do Terminal com Python

Objetivo: Ao final deste material você será capaz de criar scripts que:

    executam comandos automaticamente;
    instalam programas;
    criam projetos;
    executam Git;
    iniciam servidores;
    automatizam tarefas repetitivas;
    verificam erros;
    interagem com o usuário.




1. O que significa automatizar o terminal?

Imagine que todo dia você faz isso:

    cd Projetos
    
    python -m venv venv
    
    venv\Scripts\activate
    
    pip install django
    
    django-admin startproject sistema .
    
    python manage.py migrate
    
    python manage.py runserver


São vários comandos.


Python consegue executar todos eles sozinho.

Seu programa vira um "operador do computador".

Em vez de digitar:

    Você
    ↓
    
    Terminal
    ↓
    
    Comando
    ↓
    
    Resultado


fica:

    Python
    ↓
    
    Terminal
    
    ↓
    
    Comando
    
    ↓
    
    Resultado
    

2. O módulo mais importante: subprocess

É o módulo oficial do Python para conversar com o terminal.

    import subprocess

Ele consegue:

    executar comandos
    capturar saída
    capturar erros
    esperar terminar
    abrir programas

É o módulo moderno.

No passado usava-se:

    os.system()

Hoje quase sempre usamos:

    subprocess



3. Primeiro exemplo:

       import subprocess
    
       subprocess.run("dir", shell=True)

No Linux:

    subprocess.run("ls", shell=True)

Resultado:
    
    Pasta1
    Pasta2
    arquivo.txt

O Python pediu para o Windows executar: dir 

Entendendo linha por linha

    import subprocess
 Importa o módulo.

    subprocess.run(...)
 Executa um comando.

    "dir"
 É exatamente o que você digitaria.

    shell=True
 Diz ao Python:
 Execute usando o CMD/PowerShell.




4. Executando vários comandos:

    
        import subprocess
        
        comandos = [
            "mkdir Projeto",
            "cd Projeto",
            "python -m venv venv"
        ]
        
        for comando in comandos:
            subprocess.run(comando, shell=True)
        
Observe um detalhe importante.
Este código possui um problema.

Por quê?

Cada chamada cria um novo terminal.

Então:

    cd Projeto
não permanece.

O próximo comando volta para a pasta anterior.
Solução

Use:

    cwd=

Exemplo:

    from pathlib import Path
    import subprocess
    
    pasta = Path("Projeto")
    
    subprocess.run("python -m venv venv",
                   shell=True,
                   cwd=pasta)
               
Agora o comando acontece dentro da pasta.



5. Capturando a saída:
    
        import subprocess
        
        resultado = subprocess.run(
            "python --version",
            shell=True,
            capture_output=True,
            text=True
        )
        
        print(resultado.stdout)

Saída:

    Python 3.13.5


O objeto resultado
Possui diversas informações.

resultado.stdout
Saída normal.

resultado.stderr
Erros.

resultado.returncode
Código de retorno.


6. Verificando erros:

    
        import subprocess
        
        resultado = subprocess.run(
            "python --version",
            shell=True,
            capture_output=True,
            text=True
        )
        
        if resultado.returncode == 0:
            print("Tudo certo!")
        else:
            print("Erro.")
   
Todo comando retorna um número, 0, sucesso.

Qualquer outro número, erro.



7. Executando Git:
 

        subprocess.run("git init", shell=True)
        
        subprocess.run("git add .", shell=True)
        
        subprocess.run('git commit -m "Primeiro commit"', shell=True)


Muito usado em automações.


8. Automatizando Django: 

Imagine criar um projeto inteiro:

    subprocess.run(
        "django-admin startproject sistema .",
        shell=True
    )
    
    subprocess.run(
        "python manage.py migrate",
        shell=True
    )
    
    subprocess.run(
        "python manage.py runserver",
        shell=True
    )

Em poucos segundos tudo está pronto.

9. Abrindo programas:

Windows
    subprocess.run("notepad")
    ou
    subprocess.Popen("notepad")

Abrir calculadora
    subprocess.Popen("calc")

Abrir Paint
    subprocess.Popen("mspaint")

Abrir VS Code
    subprocess.Popen("code")




10. Diferença entre run() e Popen():

run()
    
    Python

    ↓
    
    executa
    
    ↓
    
    espera terminar
    
    ↓
    
    continua

Exemplo:

    subprocess.run("python teste.py")

Só continua depois.

Popen()
    
    Python
    
    ↓
    
    abre
    
    ↓
    
    continua imediatamente

Exemplo:
    
    subprocess.Popen("python servidor.py")

Servidor continua aberto.
Python continua executando.



11. Executando arquivos Python:


    subprocess.run("python app.py")
Ou
    subprocess.Popen("python app.py")

Muito usado em sistemas modulares.


12. Criando um instalador:
 

Imagine um arquivo chamado: instalar.py

    import subprocess
    
    pacotes = [
        "django",
        "requests",
        "pillow",
        "beautifulsoup4"
    ]
    
    for pacote in pacotes:

    print(f"Instalando {pacote}")

    subprocess.run(
        f"pip install {pacote}",
        shell=True
    )

    print("Fim.")


13. Automatizando uma máquina: 

        subprocess.run("git pull", shell=True)
        
        subprocess.run("pip install -r requirements.txt", shell=True)
        
        subprocess.run("python manage.py migrate", shell=True)
        
        subprocess.run("python manage.py collectstatic --noinput", shell=True)
        
        subprocess.run("python manage.py runserver", shell=True)

Um único arquivo prepara todo o projeto.


14. Criando menus:

        import subprocess
        
        while True:
    
        print("1 - Abrir VS Code")
        print("2 - Abrir Calculadora")
        print("3 - Sair")
    
        opcao = input("> ")
    
        if opcao == "1":
            subprocess.Popen("code")
    
        elif opcao == "2":
            subprocess.Popen("calc")
    
        elif opcao == "3":
            break
        
        
15. Capturando erros:

        resultado = subprocess.run(
            "git status",
            shell=True,
            capture_output=True,
            text=True
        )
        
        print(resultado.stdout)
        print(resultado.stderr)

Assim você consegue registrar logs para depuração



16. shell=True ou lista de argumentos?

Existem duas formas principais de chamar um programa.

Com shell:
    
    subprocess.run("python script.py", shell=True)

Sem shell (mais seguro):
    
    subprocess.run(["python", "script.py"])


Sempre que você não precisar de recursos do terminal (como dir, copy, && ou redirecionamentos), prefira a segunda forma. Ela evita problemas com espaços e reduz riscos de segurança quando há entrada do usuário.


17. Quando usar automação de terminal?

Essa técnica é ideal para:

    Criar projetos Django automaticamente.
    Executar testes.
    Fazer backup de arquivos.
    Gerenciar Git.
    Instalar dependências.
    Iniciar vários serviços de uma vez.
    Automatizar tarefas administrativas.
    Construir assistentes pessoais como a Lumi.
    Criar scripts de implantação (deploy).
    

Boas práticas:

    Prefira subprocess.run([...]) em vez de shell=True quando possível.
    
    Verifique sempre returncode para confirmar que o comando foi executado com sucesso.
    
    Capture stdout e stderr para registrar logs e facilitar a depuração.
    
    Use pathlib.Path para trabalhar com caminhos de forma portátil entre Windows, Linux e macOS.
    
    Organize comandos repetitivos em funções para reutilização.
    
    Trate exceções (try/except) quando o comando puder falhar.
    


• Projeto prático para fixação:

    Como exercício, desenvolva um Assistente de Desenvolvimento em Python com um menu interativo que permita:
    
    Criar uma pasta para um novo projeto.
    
    Criar um ambiente virtual (venv).
    
    Instalar automaticamente as dependências de um arquivo requirements.txt.
    
    Inicializar um repositório Git.
    
    Criar um projeto Django.
    
    Executar makemigrations e migrate.
    
    Abrir o projeto no VS Code.
    
    Iniciar o servidor Django.
    
    Gerar um arquivo de log com o resultado de cada comando executado.
    
    
    Esse projeto reúne praticamente todas as técnicas estudadas e é uma excelente base para construir ferramentas maiores, como um gerenciador de projetos ou sua assistente Lumi.
