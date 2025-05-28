import os
import time


# Cadastro do usuario:

ARQUIVO_USUARIOS = "usuarios.txt"

ARQUIVO_USUARIOS = "usuarios.txt"

def carregar_usuarios(): 
    usuarios = {}  
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            for linha in f:
                email, senha = linha.strip().split(";")
                usuarios[email] = senha
    return usuarios

def salvar_usuarios(usuarios): 
    with open(ARQUIVO_USUARIOS, "w") as f:
        for email, senha in usuarios.items():
            f.write(f"{email};{senha}\n")

def validar_senha(senha):
    if len(senha) < 8:
        print("Erro: A senha é muito curta (mínimo de 8 caracteres).")  
        return False
    if not any(c.isupper() for c in senha):
        print("Erro: A senha deve conter ao menos 1 letra maiúscula.")
        return False
    if not any(c.isdigit() for c in senha):
        print("Erro: A senha deve conter ao menos 1 número.")
        return False
    return True 
    
def cadastrar():
    print("\nCadastro de novo usuário:")
    usuarios = carregar_usuarios()
    email = input("Email: ")
    dominios_validos = ["@gmail.com", "@outlook.com"]
    if not any(email.endswith(dominio) for dominio in dominios_validos):
        print("Email inválido. Por favor, use apenas @gmail.com ou @outlook.com.")
        return
    if email in usuarios:
        print("Erro: E-mail já está em uso.")
        return
    senha = input("Senha: ")
    if not validar_senha(senha):
        return
    confirmar = input("Confirme a senha: ")
    if senha != confirmar:
        print("Erro: As senhas não coincidem.")
        return

    usuarios[email] = senha
    salvar_usuarios(usuarios)  
    print("Usuário cadastrado com sucesso!")

def ler_usuarios():
    usuarios = carregar_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print("Usuários cadastrados:")
    for email in usuarios:
        print(f"- {email}")

def atualizar_usuario():
    usuarios = carregar_usuarios()
    email = input("Digite o e-mail do usuário a ser atualizado: ")
    if email not in usuarios:
        print("Erro: Usuário não encontrado.")
        return

    senha_atual = usuarios[email]
    nova_senha = input("Digite a nova senha: ")
    if nova_senha == senha_atual:
        print("Erro: A nova senha não pode ser igual à senha anterior.")
        return
    if not validar_senha(nova_senha):
        return
    confirmar_senha = input("Confirme a nova senha: ")
    if nova_senha != confirmar_senha:
        print("Erro: As senhas não coincidem.")
        return
    usuarios[email] = nova_senha
    salvar_usuarios(usuarios)
    print("Senha atualizada com sucesso!")

def deletar_usuario():
    usuarios = carregar_usuarios()
    email = input("Digite o e-mail: ")

    if email not in usuarios:
        print("Erro: Usuário não encontrado.")
        return

    senha = input("Digite a senha da conta: ")
    if usuarios[email] != senha:
        print("Erro: É necessário fornecer a senha correta para excluir a conta.")
        return

    confirmacao = input("Tem certeza que deseja deletar sua conta? Digite 'SIM' para confirmar (esta operação é irreversível): ")
    if confirmacao.upper() != "SIM":
        print("Operação cancelada.")
        return

    del usuarios[email]
    salvar_usuarios(usuarios)
    print("Usuário deletado com sucesso!")
    
def login():
    print("\n Login ")
    usuarios = carregar_usuarios()
    email = input("Email: ")
    senha = input("Senha: ")
    if email in usuarios and usuarios[email] == senha:
        menu_studybuddy(email)
    else:
        print(" Erro: Usuário ou senha incorretos.")

# Menu principal StudyBuddy:

def menu_studybuddy(email):
    while True:
        print(f"  Bem-vindo!  ")                            
        print("1-Criar cronograma de estudos personalizado")
        print("2-Iniciar timer (Técnica Pomodoro)")
        print("3-Definir metas semanais de estudo")
        print("4-Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_cronograma()
        elif opcao == "2":
            timer_pomodoro()
        elif opcao == "3":
            definir_metas()
        elif opcao == "4":
            print(" Indo para menu inicial...")
            break
        else:
            print("Opção inválida,tente novamente.")

# Funcionalidades:

# 1- Criador de cronograma 

ARQUIVO_CRONOGRAMA = "cronograma_estudos.txt"

def salvar_cronograma(cronograma):
    with open(ARQUIVO_CRONOGRAMA, "a") as f:
        for dia, materia in cronograma.items():
            f.write(f"{dia}|{materia}\n")
        f.write("\n")  

def carregar_cronogramas():
    if not os.path.exists(ARQUIVO_CRONOGRAMA):
        return []

    cronogramas = []
    atual = {}

    with open(ARQUIVO_CRONOGRAMA, "r") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                if atual:
                    cronogramas.append(atual)
                    atual = {}
                continue
            partes = linha.split("|")
            if len(partes) == 2:
                dia, materia = partes
                atual[dia] = materia
        if atual:
            cronogramas.append(atual)

    return cronogramas

def criar_cronograma():
    print("Criador de cronograma de estudos:")

    cronogramas_existentes = carregar_cronogramas()
    if cronogramas_existentes:
        print("Cronogramas existentes encontrados:")
        for i, cronograma in enumerate(cronogramas_existentes, start=1):
            print(f"\nCronograma {i}:")
            for dia, materia in cronograma.items():
                print(f"{dia}: Estudar {materia}")
        opcao = input("\nDeseja criar um novo cronograma? (s/n): ").strip().lower()
        if opcao != 's':
            return

    materias = []
    while True:
        materia = input("Digite o nome da matéria (ou pressione Enter para finalizar): ")
        if materia == "":
            break
        materias.append(materia)

    if not materias:
        print("Nenhuma matéria foi adicionada. Cronograma não criado.")
        return

    dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]

    incluir_sabado = input("Deseja incluir sábado no cronograma? (s/n): ").strip().lower() == "s"
    incluir_domingo = input("Deseja incluir domingo no cronograma? (s/n): ").strip().lower() == "s"

    if incluir_sabado:
        dias_semana.append("Sábado")
    if incluir_domingo:
        dias_semana.append("Domingo")

    cronograma = {}
    print("Agora, escolha a matéria para cada dia:")
    for dia in dias_semana:
        while True:
            materia = input(f"{dia}: ").strip()
            if materia in materias:
                cronograma[dia] = materia
                break
            else:
                print("Matéria não encontrada na lista. Tente novamente.")

    salvar_cronograma(cronograma)

    print("\nCronograma personalizado gerado:")
    for dia, materia in cronograma.items():
        print(f"{dia}: Estudar {materia}.")
        
# 2- Timer pomodoro

def timer_pomodoro():
    print("\n Iniciando o Timer...")

    try:
        ciclos = int(input("Quantos ciclos você deseja fazer? (Ex: 4): "))
    except ValueError:
        print("Entrada inválida. Use apenas números inteiros.")
        return

    for ciclo in range(1, ciclos + 1):
        print(f"\n Ciclo {ciclo} - Timer de 25 minutos.")
        countdown(25 * 60)  

        if ciclo % 4 == 0:
            print(" Intervalo: 15 minutos de pausa.")
            countdown(15 * 60)  
        else:
            print(" Descanse um pouco: 5 minutos de pausa.")
            countdown(5 * 60)  

    print(" Todos os ciclos foram concluídos, bom trabalho! ")

def countdown(tempo):
    while tempo:
        mins, secs = divmod(tempo, 60)
        tempo_formatado = f"{mins:02d}:{secs:02d}"
        print(f"\r Tempo restante: {tempo_formatado}", end="")
        time.sleep(1)
        tempo -= 1

# 3- Metas semanais

ARQUIVO_METAS = "metas_estudo.txt"

def salvar_em_txt(metas, progresso):
    with open(ARQUIVO_METAS, "w") as f:
        for materia in metas:
            meta = metas[materia]
            prog = progresso.get(materia, 0)
            f.write(f"{materia}|{meta}|{prog}\n")

def carregar_de_txt():
    metas = {}
    progresso = {}
    if os.path.exists(ARQUIVO_METAS):
        with open(ARQUIVO_METAS, "r") as f:
            for linha in f:
                partes = linha.strip().split("|")
                if len(partes) == 3:
                    materia, meta, prog = partes
                    metas[materia] = float(meta)
                    progresso[materia] = float(prog)
    return metas, progresso

def definir_metas():
    print(" Definir Metas Semanais de Estudo")

    metas, progresso = carregar_de_txt()

    if metas:
        print("Metas carregadas:")
        for materia, horas in metas.items():
            print(f"- {materia}: {horas} horas (Progresso: {progresso.get(materia, 0)} horas)")
    else:
        print("  Nenhuma meta anterior encontrada. ")

    while True:
        materia = input("Digite o nome da matéria que você deseja estudar (ou pressione Enter para finalizar): ")
        if materia == "":
            break
        try:
            horas = float(input(f"Quantas horas você quer estudar de {materia} nesta semana? "))
            if horas < 0:
                print("Por favor, insira um valor positivo.")
                continue
            metas[materia] = horas
            progresso[materia] = progresso.get(materia, 0)
        except ValueError:
            print("Entrada inválida, digite um número.")

    if not metas:
        print("Nenhuma meta foi definida.")
        return

    salvar_em_txt(metas, progresso)

    print("Metas definidas:")
    for materia, horas in metas.items():
        print(f"- {materia}: {horas} horas")

    while True:
        print(" Check-in de Estudo")
        materia = input("Digite a matéria que estudou (ou pressione Enter para sair): ")
        if materia == "":
            break
        if materia not in metas:
            print("Matéria não encontrada nas metas.")
            continue
        try:
            horas = float(input("Quantas horas você estudou? "))
            if horas < 0:
                print("Digite um valor positivo.")
                continue
            progresso[materia] += horas
            salvar_em_txt(metas, progresso)
            print(f"Progresso atualizado: {progresso[materia]}/{metas[materia]} horas")
            if progresso[materia] >= metas[materia]:
                print("Meta atingida ou superada,muito bem!")
            else:
                restante = metas[materia] - progresso[materia]
                print(f"Faltam {restante:.2f} horas para atingir a meta de {materia}.")
        except ValueError:
            print("Digite um número válido.")

    print("\n Resumo do seu progresso semanal:")
    for materia in metas:
        estudado = progresso[materia]
        meta = metas[materia]
        status = "Cumprida" if estudado >= meta else "Incompleta"
        print(f"- {materia}: {estudado}/{meta} horas – {status}")

# Menu do CRUD:

def menu_crud():
    while True:
        print("\n Menu CRUD:")
        print("1.Criar usuário")
        print("2.Verificar usuários")
        print("3.Atualizar usuário")
        print("4.Deletar usuário")
        print("5.Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            ler_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do script:

def menu_inicial():
    while True:
        print("  Seja muito bem-vindo ao StudyBuddy! ")
        print("1 - Login")
        print("2 - Realizar Cadastro")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            login()
        elif opcao == "2":
            menu_crud()
        elif opcao == "3":
            print("Saindo.")
            break
        else:
            print("Opção invalida,tente novamente.")

# Iniciar o código:

menu_inicial()
