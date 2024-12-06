import sqlite3

# Criar a base de dados e a tabela para o estado de conservação
con = sqlite3.connect("carros_estado.db")
cursor = con.cursor()

# Criar a tabela com ID e Estado de Conservação
cursor.execute("""
CREATE TABLE IF NOT EXISTS carros_estado (
    id INTEGER PRIMARY KEY,
    estado_conservacao TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES carros_mae (id)
)
""")

# Inserir dados (exemplo de estados)
estados = ["Novo", "Usado", "Precisa de Reparação"]
estado_conservacao = [(i, estados[i % len(estados)]) for i in range(1, 51)]
cursor.executemany("INSERT INTO carros_estado (id, estado_conservacao) VALUES (?, ?)", estado_conservacao)

con.commit()
con.close()

print("Tabela carros_estado criada no ficheiro 'carros_estado.db'.")
