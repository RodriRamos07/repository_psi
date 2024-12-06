import sqlite3
import os
from random import randint

# Funções para `carros_mae`
def create_table_carros_mae():
    con = sqlite3.connect("carros_mae.db")
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carros_mae (
        id INTEGER PRIMARY KEY,
        marca TEXT NOT NULL
    )
    """)
    # Inserir 50 carros, se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM carros_mae")
    if cursor.fetchone()[0] == 0:
        carros = [(i, f"Marca_{i}") for i in range(1, 51)]
        cursor.executemany("INSERT INTO carros_mae (id, marca) VALUES (?, ?)", carros)
    con.commit()
    con.close()

def read_carros_mae():
    con = sqlite3.connect("carros_mae.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM carros_mae")
    rows = cursor.fetchall()
    con.close()
    return rows

def update_carros_mae(car_id, new_marca):
    con = sqlite3.connect("carros_mae.db")
    cursor = con.cursor()
    cursor.execute("UPDATE carros_mae SET marca = ? WHERE id = ?", (new_marca, car_id))
    con.commit()
    con.close()

# Funções para `carros_ano`
def create_table_carros_ano():
    con = sqlite3.connect("carros_ano.db")
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carros_ano (
        id INTEGER PRIMARY KEY,
        ano_fabrico INTEGER NOT NULL
    )
    """)
    # Inserir anos de fabrico, se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM carros_ano")
    if cursor.fetchone()[0] == 0:
        anos_fabrico = [(i, randint(2000, 2020)) for i in range(1, 51)]
        cursor.executemany("INSERT INTO carros_ano (id, ano_fabrico) VALUES (?, ?)", anos_fabrico)
    con.commit()
    con.close()

def read_carros_ano():
    con = sqlite3.connect("carros_ano.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM carros_ano")
    rows = cursor.fetchall()
    con.close()
    return rows

def update_carros_ano(car_id, new_ano):
    con = sqlite3.connect("carros_ano.db")
    cursor = con.cursor()
    cursor.execute("UPDATE carros_ano SET ano_fabrico = ? WHERE id = ?", (new_ano, car_id))
    con.commit()
    con.close()

# Funções para `carros_estado`
def create_table_carros_estado():
    con = sqlite3.connect("carros_estado.db")
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carros_estado (
        id INTEGER PRIMARY KEY,
        estado_conservacao TEXT NOT NULL
    )
    """)
    # Inserir estados de conservação, se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM carros_estado")
    if cursor.fetchone()[0] == 0:
        estados = ["Novo", "Usado", "Precisa de Reparação"]
        estado_conservacao = [(i, estados[i % len(estados)]) for i in range(1, 51)]
        cursor.executemany("INSERT INTO carros_estado (id, estado_conservacao) VALUES (?, ?)", estado_conservacao)
    con.commit()
    con.close()

def read_carros_estado():
    con = sqlite3.connect("carros_estado.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM carros_estado")
    rows = cursor.fetchall()
    con.close()
    return rows

def update_carros_estado(car_id, new_estado):
    con = sqlite3.connect("carros_estado.db")
    cursor = con.cursor()
    cursor.execute("UPDATE carros_estado SET estado_conservacao = ? WHERE id = ?", (new_estado, car_id))
    con.commit()
    con.close()

# Função principal
def main():
    print("Criando tabelas e bases de dados...")
    create_table_carros_mae()
    create_table_carros_ano()
    create_table_carros_estado()

    print("\n--- Leitura Inicial ---")
    print("\nTabela 'carros_mae':", read_carros_mae())
    print("\nTabela 'carros_ano':", read_carros_ano())
    print("\nTabela 'carros_estado':", read_carros_estado())

    print("\n--- Atualizações ---")
    print("Atualizando alguns registos...")
    update_carros_mae(1, "Marca_Atualizada")
    update_carros_ano(1, 2025)
    update_carros_estado(1, "Excelente")

    print("\n--- Leitura Após Atualizações ---")
    print("\nTabela 'carros_mae':", read_carros_mae())
    print("\nTabela 'carros_ano':", read_carros_ano())
    print("\nTabela 'carros_estado':", read_carros_estado())

    print("\nProcesso concluído.")

if __name__ == "__main__":
    main()
