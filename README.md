# StudyBuddy

StudyBuddy é um sistema de organização de estudos que oferece funcionalidades para cadastro de usuários, criação de cronogramas personalizados, definição de metas semanais e uso da técnica Pomodoro para gerenciamento do tempo.

## Funcionalidades

 1. Cadastro e Login
- Cadastro de novos usuários com validação de senha (mínimo 8 caracteres, ao menos uma letra maiúscula e um número).
- Login com verificação de e-mail e senha.
- Atualização de senha.
- Exclusão de conta com confirmação.

 2. Criador de Cronograma de Estudos
- Cadastro de matérias.
- Seleção manual de qual matéria será estudada em cada dia da semana.
- Opção de incluir sábado e domingo.
- Salvamento de múltiplos cronogramas em arquivo `.txt`.

 3. Timer Pomodoro
- Temporizador com ciclos de 25 minutos de estudo e pausas de 5 ou 15 minutos, com número de ciclos configurável.
- Usado para aplicar a técnica Pomodoro de forma prática no terminal.

 4. Metas Semanais de Estudo
- Definição de metas de horas semanais para cada matéria.
- Registro de progresso diário.
- Salvamento e atualização automática das metas e progresso.
- Resumo final com status (cumprida ou incompleta).

# Estrutura de Arquivos

- `usuarios.txt`: Armazena os e-mails e senhas dos usuários.
- `cronograma_estudos.txt`: Armazena os cronogramas criados.
- `metas_estudo.txt`: Armazena as metas e progresso de estudo.

# Como Usar

1. Execute o script Python (`python seu_script.py`).
2. No menu inicial, escolha entre login ou cadastro.
3. Após logar, acesse as funcionalidades do StudyBuddy pelo menu principal.
4. As informações são salvas automaticamente em arquivos `.txt`.

# Autor

Projeto desenvolvido por Luiz Eduardo para fins educacionais,conterá atualizações futuras.
