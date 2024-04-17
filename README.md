# API GAMER MVP

Este projeto modesto é parte do MVP **Desenvolvimento Full Stack Básico**.

O objetivo é desenvolver uma API capaz de realizar diversas operações, tais como GET/PUSH/DELETE, interagindo com um banco de dados SQLite. 
A documentação da API está disponível em Swagger.

---

## Como Executar

> Antes de executar, é altamente recomendado o uso de um ambiente virtual, como o [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Após clonar o repositório, é necessário instalar todas as bibliotecas Python listadas no arquivo `requirements.txt`. Para isso, basta acessar o diretório raiz por meio do terminal e executar os comandos apropriados.

Este comando abaixo instala as dependências ou bibliotecas descritas no arquivo. `requirements.txt`.

```
(env)$ pip install -r requirements.txt
```

Para executar a API GAMER MVP basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Durante o desenvolvimento, é aconselhável executar com o parâmetro reload, o qual reiniciará o servidor automaticamente sempre que houver uma alteração no código-fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API GAMER MVP em execução.
