import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/"

def get_all_data():
    url = BASE_URL + "pokemon?limit=1025"
    request = requests.get(url)
    if request.status_code != 200:
        print(f"ERROR {request.status_code}: Falla en obtenir les dades")
        return None
    else:
        data = request.json()
        return data["results"]

def save_json(diccionari):
    with open("pokemon_data.json", "w", encoding="utf-8") as file:
        json.dump(diccionari, file, indent=4, ensure_ascii=False)

def create_pokemons_json(pokemons):
    pokemons2return = []
    for pokemon in pokemons:
        details = requests.get(pokemon["url"]).json()
        single_poke = {
            "id": details["id"],
            "name": details["name"],
            "tipo": details["types"][0]["type"]["name"],
            "altura": details["height"],
            "img": details["sprites"]["front_default"]
        }
        pokemons2return.append(single_poke)
        print(f"Añadido el pokemon: {pokemon["name"]}")
    return pokemons2return

def main():
    pokemons = get_all_data()
    if pokemons != None:
        print(pokemons)
        save_json(create_pokemons_json(pokemons))

if __name__ == "__main__":
    main()
