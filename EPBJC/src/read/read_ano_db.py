import sqlite3

def read_carros_ano():
    con = sqlite3.connect("carros_ano.db")
    cursor = con.cursor()
    
    # Ler todos os dados da tabela carros_ano
    cursor.execute("SELECT * FROM carros_ano")
    rows = cursor.fetchall()
    con.close()
    
    print("Dados da tabela 'carros_ano':")
    for row in rows:
        print(f"ID: {row[0]}, Ano de Fabrico: {row[1]}")

# Executar
read_carros_ano()
