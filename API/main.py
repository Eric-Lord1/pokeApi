from fastapi import FastAPI, HTTPException
from datetime import date
from database import get_db_connection
from models import Pokemon, Usuari, Reserva
from typing import Optional

app = FastAPI()

# Rutes per a Pokémon
@app.post("/pokemon/")
def crear_pokemon(name: str, tipo: Optional[str] = None, altura: Optional[float] = None, img: Optional[str] = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokemon (name, tipo, altura, img) VALUES (%s, %s, %s, %s)", (name, tipo, altura, img))
    conn.commit()
    pokemon_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return Pokemon(id=pokemon_id, name=name, tipo=tipo, altura=altura, img=img)

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
    return Pokemon(id=resultat["id"], name=resultat["name"].get("name"), tipo=resultat["tipo"].get("tipo"), altura=resultat["altura"].get("altura"), img=resultat["img"].get("img"))

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
    return Usuari(id=resultat["id"], nom=resultat["nom"])

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
    return Reserva(id=resultat["id"], data_reserva=resultat["data_reserva"], numero_comanda=resultat["numero_comanda"], usuari_id=resultat["usuari_id"], pokemon_id=resultat["pokemon_id"])
