[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT) [![time tracker](https://wakatime.com/badge/github/CleysonPH/django-bookshelf.svg)](https://wakatime.com/badge/github/CleysonPH/django-bookshelf)

# Virtual Bookshelf

Projeto feito para fins de estudo, esse proejto é uma rede social para leitores que permite com que os usuários possam marcar um livro como "Lido", "Estou Lendo" e "Quero Ler", também permite que os usuários possam escrever críticas sobre os livros cadastrados no site.

## Bibliotecas utilizadas

- Django
- Django-StdImage
- Django-Bootstrap4
- Python-Decouple

## Requisitos

- Python 3.6 ou superior

## Como começar

Clone este repositório e ente na pasta do projeto

```sh
git clone https://github.com/CleysonPH/django-bookshelf.git
cd django-bookshelf
```

## Como rodar esse projeto

Inicie o ambiente virtual com o Poetry

```sh
poetry use env 3.8
poetry shell
```

Instale as dependências do projeto

```sh
poetry install
```

Crie um arquivo `.env` na raiz do projeto com as informações do banco de dados, use o arquivo `.env_exemple` como base.

Crie o banco de dados e um usuario para acessar o sistema

```sh
python manage.py makemigrations
python manage.py createsuperuser
```

E por ultimo basta executar o servidor de desenvolvimento do Django

```sh
python manage.py runserver
```

E então acessar a aplicação em http://localhost:8000/
