import sqlite3

# Criar a base de dados e a tabela mãe
con = sqlite3.connect("carros_mae.db")
cursor = con.cursor()

# Criar a tabela mãe com ID e Marca
cursor.execute("""
CREATE TABLE IF NOT EXISTS carros_mae (
    id INTEGER PRIMARY KEY,
    marca TEXT NOT NULL
)
""")

# Inserir 50 carros (exemplo)
carros = [(i, f"Marca_{i}") for i in range(1, 51)]
cursor.executemany("INSERT INTO carros_mae (id, marca) VALUES (?, ?)", carros)

con.commit()
con.close()

print("Tabela carros_mae criada no ficheiro 'carros_mae.db'.")
