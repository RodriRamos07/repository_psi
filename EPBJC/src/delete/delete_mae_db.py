import sqlite3
import os

# Remover a tabela da base de dados
def delete_table_carros_mae():
    con = sqlite3.connect("carros_mae.db")
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS carros_mae")
    con.commit()
    con.close()
    print("Tabela 'carros_mae' apagada.")

# Apagar o ficheiro físico da base de dados
def delete_file_carros_mae():
    if os.path.exists("carros_mae.db"):
        os.remove("carros_mae.db")
        print("Ficheiro 'carros_mae.db' apagado.")
    else:
        print("Ficheiro 'carros_mae.db' não existe.")

# Executar
delete_table_carros_mae()
delete_file_carros_mae()
