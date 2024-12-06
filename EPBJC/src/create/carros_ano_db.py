import sqlite3

# Criar a base de dados e a tabela para o ano de fabrico
con = sqlite3.connect("carros_ano.db")
cursor = con.cursor()

# Criar a tabela com ID e Ano de Fabrico
cursor.execute("""
CREATE TABLE IF NOT EXISTS carros_ano (
    id INTEGER PRIMARY KEY,
    ano_fabrico INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES carros_mae (id)
)
""")

# Inserir dados (exemplo: ano aleatório entre 2000 e 2020)
from random import randint

anos_fabrico = [(i, randint(2000, 2020)) for i in range(1, 51)]
cursor.executemany("INSERT INTO carros_ano (id, ano_fabrico) VALUES (?, ?)", anos_fabrico)

con.commit()
con.close()

print("Tabela carros_ano criada no ficheiro 'carros_ano.db'.")
