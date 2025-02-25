from fastapi import FastAPI, HTTPException
from datetime import date
from database import get_db_connection
from models import Pokemon, Usuari, Reserva

app = FastAPI()

# Rutes per a Pokémon
@app.post("/pokemon/")
def crear_pokemon(nom: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokemon (nom) VALUES (%s)", (nom,))
    conn.commit()
    pokemon_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return Pokemon(id=pokemon_id, nom=nom)

@app.get("/pokemon/{pokemon_id}")
def obtenir_pokemon(pokemon_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemon WHERE id = %s", (pokemon_id,))
    resultat = cursor.fetchone()
    cursor.close()
    conn.close()
    if not resultat:
        raise HTTPException(status_code=404, detail="Pokemon no trobat")
    return Pokemon(**resultat)

# Rutes per a Usuaris
@app.post("/usuari/")
def crear_usuari(nom: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuari (nom) VALUES (%s)", (nom,))
    conn.commit()
    usuari_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return Usuari(id=usuari_id, nom=nom)

@app.get("/usuari/{usuari_id}")
def obtenir_usuari(usuari_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuari WHERE id = %s", (usuari_id,))
    resultat = cursor.fetchone()
    cursor.close()
    conn.close()
    if not resultat:
        raise HTTPException(status_code=404, detail="Usuari no trobat")
    return Usuari(**resultat)

# Rutes per a Reserves
@app.post("/reserva/")
def crear_reserva(data_reserva: date, numero_comanda: str, usuari_id: int, pokemon_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reserva (data_reserva, numero_comanda, usuari_id, pokemon_id)
        VALUES (%s, %s, %s, %s)
    """, (data_reserva, numero_comanda, usuari_id, pokemon_id))
    conn.commit()
    reserva_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return Reserva(id=reserva_id, data_reserva=data_reserva, numero_comanda=numero_comanda, usuari_id=usuari_id, pokemon_id=pokemon_id)

@app.get("/reserva/{reserva_id}")
def obtenir_reserva(reserva_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reserva WHERE id = %s", (reserva_id,))
    resultat = cursor.fetchone()
    cursor.close()
    conn.close()
    if not resultat:
        raise HTTPException(status_code=404, detail="Reserva no trobada")
    return Reserva(**resultat)
