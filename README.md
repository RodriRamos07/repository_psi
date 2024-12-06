Estrutura recomendada para o projeto final do módulo 15:

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
│   ├── epbjc_backup_1.db
│   ├── epbjc_backup_2.db
│   └── epbjc_backup_3.db
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
