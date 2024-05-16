FastAPI TDD Project
Este é um projeto de exemplo para demonstrar o desenvolvimento de uma API usando o framework FastAPI com a metodologia TDD (Test-Driven Development). O objetivo é criar uma API simples para gerenciar itens, com operações CRUD (Create, Read, Update, Delete) para adicionar, listar, visualizar, atualizar e excluir itens.

Funcionalidades da API
A API possui os seguintes endpoints:

POST /items/: Cria um novo item.
GET /items/: Lista todos os itens.
GET /items/{item_id}: Retorna os detalhes de um item específico.
PUT /items/{item_id}: Atualiza os detalhes de um item existente.
DELETE /items/{item_id}: Exclui um item existente.
Pré-requisitos
Python 3.9 ou superior
Docker (opcional, para rodar a aplicação em um contêiner)
Instalação e Execução
Clone o repositório para o seu ambiente local:

bash
Copiar código
git clone https://github.com/seu-usuario/fastapi-tdd-project.git
Navegue até o diretório do projeto:

bash
Copiar código
cd fastapi-tdd-project
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

No Windows:

bash
Copiar código
venv\Scripts\activate
No macOS e Linux:

bash
Copiar código
source venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Execute os testes para garantir que tudo está funcionando corretamente:

bash
Copiar código
pytest
Inicie a aplicação:

bash
Copiar código
uvicorn app.main:app --host 0.0.0.0 --port 8000
Se preferir, você pode usar o Docker para rodar a aplicação em um contêiner. Certifique-se de ter o Docker instalado e configurado corretamente. Use os comandos descritos no arquivo Dockerfile para construir e rodar o contêiner.
Acesse a API em http://localhost:8000 e a documentação interativa em http://localhost:8000/docs para testar os endpoints.

Estrutura do Projeto
app/main.py: Arquivo principal da aplicação FastAPI, contendo a definição dos endpoints e a lógica de negócio.
tests/test_main.py: Arquivo de testes, contendo os testes para os endpoints da API.
requirements.txt: Lista das dependências necessárias para executar o projeto.
Dockerfile: Arquivo de configuração do Docker para construir a imagem da aplicação.
Contribuindo
Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request. Sua contribuição é muito bem-vinda!

Licença
Este projeto é distribuído sob a licença MIT.