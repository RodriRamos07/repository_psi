import sqlite3

def update_carros_mae(car_id, new_marca):
    con = sqlite3.connect("carros_mae.db")
    cursor = con.cursor()
    
    # Atualizar a marca do carro com o ID fornecido
    cursor.execute("UPDATE carros_mae SET marca = ? WHERE id = ?", (new_marca, car_id))
    con.commit()
    con.close()
    
    print(f"Marca do carro com ID {car_id} atualizada para '{new_marca}'.")

# Exemplo: Atualizar o carro com ID 1 para "Marca_Atualizada"
update_carros_mae(1, "Marca_Atualizada")
