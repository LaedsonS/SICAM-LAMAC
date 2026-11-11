O projeto tem como objetivo desenvolver um software voltado ao gerenciamento e cadastro de máquinas e suas manutenções no LAMAC (Laboratório de Manutenção de Computadores) no IFRN Campus SGA, proporcionando maior organização, agilidade e segurança no armazenamento das informações relacionadas aos equipamentos no local.

Para a execução do projeto, é necessário seguir os  seguintespassos:

**1. Clonar o repositório**

    git clone h[ttps://github.com/usuario/projeto_tasks.git](https://github.com/LaedsonS/SICAM-LAMAC.git)

**2. Criar o ambiente virtual**

    python -m venv ./venv
  
  Ative o ambiente:
  
  No Windows:  
  
    venv\Scripts\activate
  
  No Linux ou Mac: 
  
    source venv/bin/activate

**3. Instalar as dependências**

    pip install -r requirements.txt
  
  (Isso instala o Django e o python-dotenv de uma só vez)

**4. Criar o arquivo .env**
  
  Copie o arquivo modelo e renomeie para .env:
  
    cp .env.example .env
  
  No Windows, se o comando cp não funcionar:
  
    copy .env.example .env
  
  Abra o .env. Ele contém:
    SECRET_KEY=
    DEBUG=True 

**5. Gerar uma SECRET_KEY**

    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

  O terminal imprimirá uma chave aleatória, como:
  
    django-insecure-9x#k2$m4v@q7w8e9r1t2y3u4i5o6p7a8s9d0f1g2h3j4k5l6

**6. Colar a chave no .env**

Copie a chave impressa e cole no arquivo (sem aspas e sem espaços):

  SECRET_KEY=django-insecure-9x#k2$m4v@q7w8e9r1t2y3u4i5o6p7a8s9d0f1g2h3j4k5l6
  DEBUG=True

**7. criar o banco de dados**

    python manage.py migrate

**8. Rodar o projeto**

    python manage.py runserver

  Acesse http://localhost:8000/ no navegador.
