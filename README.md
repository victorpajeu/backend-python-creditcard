# Sistema de Cartão de Crédito

Este é um sistema simples de cartão de crédito desenvolvido com Django.

## Pré-requisitos

Certifique-se de ter o Docker e o Docker Compose instalados no seu sistema.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Como Usar

1. **Clone este repositório:**

    ```bash
    git clone https://github.com/seu-usuario/backend-python-creditcard.git
    cd backend-python-creditcard
    ```

2. **Construa e execute o contêiner Docker:**

    ```bash
    docker-compose up --build
    ```

    Este comando irá construir a imagem Docker, criar os contêineres e iniciar o sistema.

3. **Acesse o Admin do Django:**

    Abra um navegador e acesse [http://localhost:8000/admin/](http://localhost:8000/admin/). Use as credenciais:

    - **Usuário:** admin
    - **Senha:** admin

    Essas credenciais foram configuradas automaticamente durante a inicialização.

4. **Interaja com a API:**

    Você pode interagir com a API acessando [http://localhost:8000/api/v1/credit-card/](http://localhost:8000/api/v1/credit-card/) ou usar ferramentas como o [Postman](https://www.postman.com/) para testar as operações da API.

## Encerrando

Para encerrar o sistema, pressione `Ctrl + C` no terminal onde você executou o `docker-compose up` e execute:

```bash
docker-compose down
