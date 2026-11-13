## 1. Título do projeto: 

  # SISTEMA DE CADASTRO PARA A MANUTENÇÃO DE MÁQUINAS NO LAMAC (SICAM-LAMAC)

## 2. Descrição
   No Laboratório de Manutenção de Computadores (LAMAC), há excesso notebooks, PCs, e outros equipamento eletrônicos largados aleatoriamente com defeitos e sem identificação no ambientes. Com isso, surge a ideia de um software que cadastre máquinas e suas manutenções para a organização do ambiente.

## 3. Objetivos
O projeto tem como objetivo desenvolver um software voltado ao gerenciamento e cadastro de máquinas e suas manutenções no LAMAC no IFRN Campus SGA, proporcionando maior organização, agilidade e segurança no armazenamento das informações relacionadas aos equipamentos no local.

## 4. Funcionalidades

* Os usuários podem criar uma solicitação para o cadastro da máquina no sistema.
* Os usuários podem fazer login no sistema.
* Os usuários podem pesquisar máquinas cadastradas.
* Os clientes podem cadastrar seus computadores.
* Os técnicos podem remover máquinas cadastradas pelo cliente.
* Os técnicos podem editar as informações das máquinas cadastradas.
* O técnicos podem registrar as manutenções após serem realizadas.
* Os técnicos podem consultar o histórico de manutenção de todas as máquinas.

## 5. Tecnologias utilizadas
  
* Python
* Django
* HTML e CSS
* JavaScript
* Bootstrap
* SQLite
* python-dotenv


## 6. Pré-requisitos: 

1. Conhecimentos básicos
    * Python: variáveis, funções, classes, módulos, listas e dicionários. 
    * HTML e CSS
    * Banco de dados e SQL (tabelas, chaves primárias e estrangeiras e relacionamentos)
    * HTTP (GET, POST e códigos de status)
    * Linha de comando

2. Ferramentas a instalar
    * Python 3
    * pip
    * Ambiente virtual (venv)
    * VS Code
    * Git

## 7. Instalação e execução
  Para a execução do projeto, é necessário seguir os  seguintes passos:

  **7.1. Clonar o repositório**

    git clone h[ttps://github.com/usuario/projeto_tasks.git](https://github.com/LaedsonS/SICAM-LAMAC.git)

  **7.2. Criar o ambiente virtual**

    python -m venv ./venv
      
Ative o ambiente:
      
No Windows:  
      
    venv\Scripts\activate
      
No Linux ou Mac: 
      
    source venv/bin/activate

  **7.3. Instalar as dependências**

      pip install -r requirements.txt
      
(Isso instala o Django e o python-dotenv de uma só vez)

  **7.4. Criar o arquivo .env**
      
<<<<<<< HEAD
crie o arquivo *.env*
=======
Copie o arquivo modelo e renomeie para .env:
      
      cp .env.example .env
      
No Windows, se o comando cp não funcionar:
      
      copy .env.example .env
>>>>>>> 3dacf3f52c709b24f6a5985c5536dabcaadc18b2
      
Abra o **.env**, ele deve conter:
      SECRET_KEY=
      DEBUG=True 

  **7.5. Gerar uma SECRET_KEY**

      python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

O terminal imprimirá uma chave aleatória, como:
      
      django-insecure-9x#k2$m4v@q7w8e9r1t2y3u4i5o6p7a8s9d0f1g2h3j4k5l6

  **7.6. Colar a chave no .env**

  Copie a chave impressa no terminal e cole no arquivo (sem aspas e sem espaços):

    SECRET_KEY=django-insecure-9x#k2$m4v@q7w8e9r1t2y3u4i5o6p7a8s9d0f1g2h3j4k5l6
    DEBUG=True

  **7.7. criar o banco de dados**

      python manage.py migrate

  **7.8. Rodar o projeto**

      python manage.py runserver

Acesse http://localhost:8000/ no navegador.

## 8. Estrutura do projeto
   
        ├── maquinas/              # App de tarefas
        │   ├── models.py
        │   ├── views.py
        │   ├── urls.py
        │   └── migrations/
        ├── setup/                # Configurações do projeto
        │   ├── settings.py
        │   ├── urls.py
        │   ├── asgi.py
        │   └── wsgi.py
        ├── static/               # CSS, JS e imagens
        │   ├── css/
        │   ├── js/
        │   └── img/
        ├── templates/            # Arquivos HTML
        │   ├── maquina/
        │   ├── usuarios/
        │   └── base.html
        ├── usuarios/             # App de usuários
        │   ├── models.py
        │   ├── views.py
        │   ├── urls.py
        │   └── migrations/
        ├── venv/                 # Ambiente virtual (não vai para o GitHub)
        ├── .env                  # Variáveis de ambiente (não vai para o GitHub)
        ├── .gitignore
        ├── .env.example          # Modelo do .env (vai para o GitHub)
        ├── manage.py
        ├── README.md
        ├── requirements.txt

## 9. Equipe
    
* Laedson Santos da Costa
* Yohana Larissa da Rocha Venancio
* Ana Julia Anulino da Silva

