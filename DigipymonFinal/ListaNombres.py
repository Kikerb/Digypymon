import random


class ListaNombres:
    def __init__(self):
        # Constructor por defecto con listas de nombres de Digipymons y entrenadores
        self.lista_nombres_digipymons_agua= [
            "Aqua","Marina","Nereida","Ondina","Coral","Azulin",
            "Nixie","Laguna","Aguamarina","Marea"
        ]
        self.lista_nombres_digipymons_planta= [
            "Verdant","Florin","Bosque","Folium","Espora","Clorofila",
            "Hojaverde","Raiz","Brote","Sylvan"
        ]
        self.lista_nombres_digipymons_fuego= [
            "Ignis","Pyro","Fenix","Clida","Aidan","Brasa",
            "Chispa","Ember","Infierno","Vulcano"
        ]
        self.lista_nombres_entrenadores = [
            "Ash", "Misty", "Brock", "May", "Dawn",
            "Gary", "Serena", "Clemont", "Lillie", "Kiawe",
            "Jessie", "James", "Professor Oak", "Tracey", "Iris",
            "Cilan", "Max", "Bonnie", "Sophocles", "Mallow"
        ]

    def obtener_nombre_digipymon_agua(self):
        # Obtener un nombre aleatorio de la lista de nombres de Digipymons de agua
        return random.choice(self.lista_nombres_digipymons_agua)
    def obtener_nombre_digipymon_fuego(self):
        # Obtener un nombre aleatorio de la lista de nombres de Digipymons de fuego
        return random.choice(self.lista_nombres_digipymons_fuego)
    def obtener_nombre_digipymon_planta(self):
        # Obtener un nombre aleatorio de la lista de nombres de Digipymons de planta
        return random.choice(self.lista_nombres_digipymons_planta)

    def obtener_nombre_entrenador(self):
        # Obtener un nombre aleatorio de la lista de nombres de entrenadores
        return random.choice(self.lista_nombres_entrenadores)