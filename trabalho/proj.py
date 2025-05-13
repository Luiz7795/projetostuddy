import os


# Cadastro do usuario

ARQUIVO_USUARIOS = "usuarios.txt"

def carregar_usuarios(): 
    usuarios = {}  # Cria um txt vazio para guardar nomes e senhas
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            for linha in f:
                usuario, senha = linha.strip().split(";")
                usuarios[usuario] = senha
    return usuarios

def salvar_usuario(usuario, senha):
    with open(ARQUIVO_USUARIOS, "a") as f:
        f.write(f"{usuario};{senha}\n") # Salva o usuario e a senha do cadastro

def cadastrar():
    print("\n Cadastro de Novo Usuário ")
    usuarios = carregar_usuarios()
    usuario = input("Novo usuário: ")
    if usuario in usuarios:
        print("Erro: Usuário já existe.")
        return
    senha = input("Senha: ")
    salvar_usuario(usuario, senha)
    print("Usuário cadastrado com sucesso!")

def login():
    print("\n Login ")
    usuarios = carregar_usuarios()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido! Bem-vindo,", usuario)
        menu_studybuddy(usuario)
    else:
        print("Erro: Usuário ou senha incorretos.")

# Menu principal StudyBuddy

def menu_studybuddy(usuario):
    while True:
        print(f"n/Bem-vindo ao StudyBuddy!")                            
        print("1-Criar cronograma de estudo automatico")
        print("2-Iniciar timer (Tecnica Pomodoro)")
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

# Funcionalidades

def criar_cronograma():
    print("\n criando cronograma automatico...")
    materias = ["Matematica", "Portugues", "historia", "fisica", "Ingles"]
    for i, materia in enumerate(materias, 1):
        print(f"Dia {i}: Estudar {materia}")

# Execucao do script

def menu_inicial():
    while True:
        print("\n Bem vindo ao StudyPal! ")
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

# Iniciar o programa

menu_inicial()