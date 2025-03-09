from database import get_db_connection

def inicialitzar_bbdd():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(100) NOT NULL,
        altura DECIMAL(5, 2),
        tipo VARCHAR(50),
        img VARCHAR(255)
    ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuari (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100) NOT NULL
            ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reserva (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data_reserva DATE NOT NULL,
            numero_comanda VARCHAR(50) NOT NULL,
            usuari_id INT,
            pokemon_id INT,
            FOREIGN KEY (usuari_id) REFERENCES usuari(id),
            FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
        ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """)

    conn.commit()
    cursor.close()
    conn.close()
                                            
    print("Base de datos inicializada correctamente.")

if __name__ == "__main__":
    inicialitzar_bbdd()
