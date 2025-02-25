-- Utilitza la base de dades pokemon_db
USE pokedb;

-- Inserts per a la taula `pokemon`
INSERT INTO pokemon (nom) VALUES ('Pikachu');
INSERT INTO pokemon (nom) VALUES ('Bulbasaur');
INSERT INTO pokemon (nom) VALUES ('Charmander');
INSERT INTO pokemon (nom) VALUES ('Squirtle');
INSERT INTO pokemon (nom) VALUES ('Eevee');

-- Inserts per a la taula `usuari`
INSERT INTO usuari (nom) VALUES ('Ash Ketchum');
INSERT INTO usuari (nom) VALUES ('Misty');
INSERT INTO usuari (nom) VALUES ('Brock');
INSERT INTO usuari (nom) VALUES ('Gary Oak');
INSERT INTO usuari (nom) VALUES ('Professor Oak');

-- Inserts per a la taula `reserva`
-- Nota: Les dates estan en format 'YYYY-MM-DD'
INSERT INTO reserva (data_reserva, numero_comanda, usuari_id, pokemon_id) VALUES ('2023-10-01', 'ORD123', 1, 1);
INSERT INTO reserva (data_reserva, numero_comanda, usuari_id, pokemon_id) VALUES ('2023-10-02', 'ORD124', 2, 2);
INSERT INTO reserva (data_reserva, numero_comanda, usuari_id, pokemon_id) VALUES ('2023-10-03', 'ORD125', 3, 3);
INSERT INTO reserva (data_reserva, numero_comanda, usuari_id, pokemon_id) VALUES ('2023-10-04', 'ORD126', 4, 4);
INSERT INTO reserva (data_reserva, numero_comanda, usuari_id, pokemon_id) VALUES ('2023-10-05', 'ORD127', 5, 5);
INSERT INTO reserva (data_reserva, numero_comanda, usuari_id, pokemon_id) VALUES ('2023-10-06', 'ORD128', 1, 2);
INSERT INTO reserva (data_reserva, numero_comanda, usuari_id, pokemon_id) VALUES ('2023-10-07', 'ORD129', 2, 3); 
