# Tools

## Instalação

Apos clonar o projeto seguir passos abaixo:

### Criar ambiente virtual:
    python -m venv venv 

### Ativar Ambiente Virtual
    source venv/bin/activate

### Com o ambiente virtual ativo instalar dependencias:
    pip install -r requirements.txt

### Renomeie o arquivo .env_exemple para .env e preencha os itens nele.

### Rode as migrations
    python manage.py makemigrations
    python manage.py migrate

### Crie o super user para a area de admin e preencha o que se pede:
    python manage.py createsuperuser

### Inicie o servidor:
    python manage.py runserver

