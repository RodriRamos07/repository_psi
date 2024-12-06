import sqlite3

def read_carros_mae():
    con = sqlite3.connect("carros_mae.db")
    cursor = con.cursor()
    
    # Ler todos os dados da tabela carros_mae
    cursor.execute("SELECT * FROM carros_mae")
    rows = cursor.fetchall()
    con.close()
    
    print("Dados da tabela 'carros_mae':")
    for row in rows:
        print(f"ID: {row[0]}, Marca: {row[1]}")

# Executar
read_carros_mae()
