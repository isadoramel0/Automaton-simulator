# Automaton Simulator

Este repositório contém um simulador de autômatos que permite a criação, execução e teste de diferentes tipos de autômatos, utilizando FastAPI para fornecer uma API RESTful.

## 📌 Requisitos

Antes de rodar o projeto, certifique-se de ter os seguintes requisitos instalados:

- 🐍 Python 3.8 ou superior
- 🛠️ Git
- ⚡ FastAPI
- 🔥 Uvicorn
- 📊 Graphviz (necessário para visualização de autômatos)
- 📖 Automata-lib

## 📥 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/isadoramel0/Automaton-simulator.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd Automaton-simulator
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Como Executar

Para iniciar a API FastAPI, utilize o seguinte comando:
```bash
uvicorn main:app --reload
```
A API estará disponível em `http://127.0.0.1:8000/docs`.

## 🔗 Endpoints da API

A API fornece suporte a três tipos de autômatos:
- 🎭 **Autômato Finito Determinístico (AFD)**
- 🏛️ **Autômato com Pilha Determinístico (APDA)**
- 🏗️ **Máquina de Turing Determinística**

### 🔹 Endpoints Gerais

- `GET /{automata}/{id}` 
  - Retorna um autômato específico pelo ID.
  - **Parâmetros:** `id` do autômato na URL.

- `POST /{automata}/{id}/test` 
  - Testa uma string no autômato especificado.
  - **Parâmetros:** `id` do autômato na URL.
  - **Corpo da requisição:** JSON contendo a string a ser testada.
  - **Exemplo de JSON:**
    ```json
    {
      "input_string": "abba"
    }
    ```
  - **Resposta:** Indica se a string é aceita ou rejeitada pelo autômato.

- `GET /{automata}/graph`
  - Retorna um grafo visual do {automato}
    
### 🔹 Endpoints Específicos

- `POST /finite-automaton/` 🎭
  - Cria um novo Autômato Finito Determinístico (AFD).
  - **Parâmetros:** JSON contendo a definição do AFD, incluindo estados, transições e estado inicial.
  
- `POST /pushdown-automaton/` 🏛️
  - Cria um novo Autômato com Pilha Determinístico (APDA).
  - **Parâmetros:** JSON contendo a definição do APDA, incluindo pilha, transições e estados finais.
  
- `POST /turing-machine/` 🏗️
  - Cria uma nova Máquina de Turing.
  - **Parâmetros:** JSON contendo a definição da máquina, incluindo fitas, transições e estados finais.

Para explorar a API interativamente, acesse `http://127.0.0.1:8000/docs`.

## ✅ Testes

Para exemplos de testes, utilize:
```bash
past:  /examples
```


Este README pode ser atualizado conforme necessário para refletir novas funcionalidades ou instruções de uso. 

