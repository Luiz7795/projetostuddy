import os


# Cadastro do usuario:

ARQUIVO_USUARIOS = "usuarios.txt"

def carregar_usuarios(): 
    usuarios = {}  # Cria um txt vazio para guardar nomes e senhas
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            for linha in f:
                email, senha = linha.strip().split(";")
                usuarios[email] = senha
    return usuarios

def salvar_usuario(email, senha):
    with open(ARQUIVO_USUARIOS, "a") as f:
        f.write(f"{email};{senha}\n") # Salva o usuario e a senha do cadastro

def cadastrar():
    print("\n Cadastro de Novo Usuário: ")
    usuarios = carregar_usuarios()
    email = input("Email: ")
    dominios_validos = ["@gmail.com","@outlook.com"]
    if not any(email.endswith(dominio) for dominio in dominios_validos):
        print ("Email inválido,porfavor use apenas @gmail.com ou @outlook.com")
        return
    if email in usuarios:
        print(" Erro: Email já está sendo utilizado,tente novamente com outro email.")
        return
    senha = input("Senha: ")
    confirmar = input("Confirme a senha: ")

    if senha != confirmar:
        print("Erro: As senhas não coincidem.")
        return

    if len(senha) < 8:
        print(" Erro: A senha é muito curta (Mínimo de 8 caracteres).")  
        return
    if not any(c.isupper() for c in senha):
        print(" Erro: A senha deve conter ao menos 1 letra maiúscula.")
        return
    if not any(c.isdigit() for c in senha):
        print(" Erro: A senha deve conter ao menos 1 número.")
        return

    salvar_usuario(email, senha)
    print("Usuário cadastrado com sucesso!")

def login():
    print("\n Login ")
    usuarios = carregar_usuarios()
    email = input("Email: ")
    senha = input("Senha: ")
    if email in usuarios and usuarios[email] == senha:
        print("Login bem-sucedido! Bem-vindo!")
        menu_studybuddy(email)
    else:
        print(" Erro: Usuário ou senha incorretos.")

# Menu principal StudyBuddy:

def menu_studybuddy(email):
    while True:
        print(f"n/Bem-vindo ao StudyBuddy!")                            
        print("1-Criar cronograma de estudo personalizado")
        print("2-Iniciar timer (Técnica Pomodoro)")
        print("3-Definir metas semanais")
        print("4-Sair")

        opcao = input("Escolha uma opçao: ")

        if opcao == "1":
            criar_cronograma()
        elif opcao == "2":
            print(" Def a ser adicionada.")
            # Futura def a ser adicionada
        elif opcao == "3":
            print(" Def a ser adicionada.")
            # Futura def a ser adicionada
        elif opcao == "4":
            print(" Saindo do StudyBuddy.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Funcionalidades:

def criar_cronograma():
    print("\n Criador de Cronograma de Estudo Personalizado")
    dias_semana = ["Segunda", "Terça", "Quarta", 
                   "Quinta", "Sexta"]
    
    incluir_sabado = input("Deseja incluir sábado no cronograma? (s/n): ").lower() == "s"
    incluir_domingo = input("Deseja incluir domingo no cronograma? (s/n): ").lower() == "s"

    if incluir_sabado:
        dias_semana.append("Sábado")
    if incluir_domingo:
        dias_semana.append("Domingo")
    
    cronograma = {}

    for dia in dias_semana:
        materia = input(f"Qual matéria você quer estudar na {dia}? ")
        cronograma[dia] = materia

    print("\n Seu cronograma ficou assim:")
    for dia, materia in cronograma.items():
        print(f"{dia}: {materia}")

# Execucao do script:

def menu_inicial():
    while True:
        print("\n Bem vindo ao StudyBuddy! ")
        print("1 - Login")
        print("2 - Cadastrar")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            login()
        elif opcao == "2":
            cadastrar()
        elif opcao == "3":
            print("Saindo.")
            break
        else:
            print("Opçao invalida.")

# Iniciar o script:

menu_inicial()
