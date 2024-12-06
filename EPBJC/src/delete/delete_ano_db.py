import sqlite3
import os

# Remover a tabela da base de dados
def delete_table_carros_ano():
    con = sqlite3.connect("carros_ano.db")
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS carros_ano")
    con.commit()
    con.close()
    print("Tabela 'carros_ano' apagada.")

# Apagar o ficheiro físico da base de dados
def delete_file_carros_ano():
    if os.path.exists("carros_ano.db"):
        os.remove("carros_ano.db")
        print("Ficheiro 'carros_ano.db' apagado.")
    else:
        print("Ficheiro 'carros_ano.db' não existe.")

# Executar
delete_table_carros_ano()
delete_file_carros_ano()
