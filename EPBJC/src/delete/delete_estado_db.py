import sqlite3
import os

# Remover a tabela da base de dados
def delete_table_carros_estado():
    con = sqlite3.connect("carros_estado.db")
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS carros_estado")
    con.commit()
    con.close()
    print("Tabela 'carros_estado' apagada.")

# Apagar o ficheiro físico da base de dados
def delete_file_carros_estado():
    if os.path.exists("carros_estado.db"):
        os.remove("carros_estado.db")
        print("Ficheiro 'carros_estado.db' apagado.")
    else:
        print("Ficheiro 'carros_estado.db' não existe.")

# Executar
delete_table_carros_estado()
delete_file_carros_estado()

