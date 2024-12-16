# Estrutura e Funcionalidade do Projeto

Este projeto é uma aplicação que utiliza SQLite para gerir bases de dados relacionadas com informações de carros.
A estrutura do projeto foi organizada de forma modular para suportar operações de criação, leitura, atualização e eliminação (CRUD).

## Estrutura de Diretórios

epbjc/
├── src/
│   ├── app/
│   │   └── main.py                         #Iniciar o código e criar tabelas se não existirem
│   ├── create/
│   │   ├── carros_ano_db.py                #Query INSERT para criar tabela carros_ano
│   │   ├── carros_estado_db.py             #Query INSERT para criar tabela carros_estado
│   │   └── professores_create_db.py        #Query INSERT para criar tabela carros_mae
│   ├── delete/
│   │   ├── delete_ano_db.py                #Query DELETE para apagar dados na tabela carros_ano
│   │   ├── delete_estado_db.py             #Query DELETE para apagar dados na tabela carros_estado
│   │   └── delete_mae_db.py                #Query DELETE para apagar dados na tabela carros_mae
│   ├── read/
│   │   ├── read_ano_db.py                  #Query SELECT para extrair dados na tabela carros_ano
│   │   ├── read_estado_db.py               #Query SELECT para extrair dados na tabela carros_estado
│   │   └── read_mae_db.py                  #Query SELECT para extrair dados na tabela carros_mae
│   └── update/
|       ├── update_ano_db.py                #Query UPDATE para atualizar os dados na tabela carros_ano
|       ├── update_estado_db.py.py          #Query UPDATE para atualizar os dados na tabela carros_estado
|       └── update_mae_db.py.py             #Query UPDATE para atualizar os dados na tabela carros_mae
├── sqlite-database/
│   ├── epbjc_backup_1.db                   #Guardar backups de código
│   ├── epbjc_backup_2.db                   #Guardar backups de código
│   └── epbjc_backup_3.db                   #Guardar backups de código
│   ├── epbjc.db
├── migracao/
│   ├── 
│   ├── 
│   ├── 
│   └── 
├── testes/
│   ├── 
│   ├── 
│   ├── 
│   └── 
└── README.md



## Arquivo `main.py`

### Funcionalidades

O script principal implementa três tabelas relacionadas com carros: `carros_mae`, `carros_ano` e `carros_estado`.

1. **`carros_mae`**:
   - **Criação da Tabela**: A tabela armazena informações sobre a marca dos carros.
   - **Leitura**: Extrai todas as marcas armazenadas.
   - **Atualização**: Atualiza a marca de um carro específico.

2. **`carros_ano`**:
   - **Criação da Tabela**: Contém informações sobre o ano de fabrico dos carros.
   - **Leitura**: Extrai os anos de fabrico.
   - **Atualização**: Permite atualizar o ano de fabrico de um carro.

3. **`carros_estado`**:
   - **Criação da Tabela**: Mantém dados sobre o estado de conservação dos carros.
   - **Leitura**: Obtém os estados de conservação.
   - **Atualização**: Atualiza o estado de conservação de um carro.

### Estrutura do Código

- Importação de bibliotecas: `sqlite3`, `os`, e `randint` para manipulação da base de dados e geração de dados aleatórios.
- **Criação das tabelas**: Cada tabela possui uma função específica para criação e preenchimento inicial.
- **Leitura dos dados**: Funções para extrair informações de cada tabela.
- **Atualização dos dados**: Permite modificar os registos existentes.

### Fluxo Principal

1. Criação das tabelas e inserção de dados iniciais.
2. Leitura e exibição dos dados iniciais.
3. Atualizações nos registos.
4. Exibição dos dados atualizados.

### Execução

O código pode ser executado diretamente utilizando o comando:

```bash
python main.py
```
