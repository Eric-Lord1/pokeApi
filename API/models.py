from datetime import date
from typing import Optional

class Pokemon:
    def __init__(self, id: Optional[int] = None, nom: Optional[str] = None, tipo: Optional[str] = None, 
                 altura: Optional[int] = None, img: Optional[str] = None):
        self.id = id
        self.nom = nom
        self.tipo = tipo
        self.altura = altura
        self.img = img

    def __repr__(self):
        return f"Pokemon(id={self.id}, nom={self.nom}, tipo={self.tipo}, altura={self.altura}, img={self.img})"

class Usuari:
    def __init__(self, id: Optional[int] = None, nom: Optional[str] = None):
        self.id = id
        self.nom = nom

    def __repr__(self):
        return f"Usuari(id={self.id}, nom={self.nom})"

class Reserva:
    def __init__(
        self,
        id: Optional[int] = None,
        data_reserva: Optional[date] = None,
        numero_comanda: Optional[str] = None,
        usuari_id: Optional[int] = None,
        pokemon_id: Optional[int] = None,
    ):
        self.id = id
        self.data_reserva = data_reserva
        self.numero_comanda = numero_comanda
        self.usuari_id = usuari_id
        self.pokemon_id = pokemon_id

    def __repr__(self):
        return f"Reserva(id={self.id}, data_reserva={self.data_reserva}, numero_comanda={self.numero_comanda}, usuari_id={self.usuari_id}, pokemon_id={self.pokemon_id})"
