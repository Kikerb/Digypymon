class Jugador():
    MAX_digipimon = 6 # Máximo número de Digipymons permitidos
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.digicoins = 10  # Número de Digicoins iniciales
        self.inventario = {}
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        
    def añadir_digipymon(self, digipymon):
        if self.cantidad_digipymon < self.MAX_digipimon:
            self.lista_digipymon.append(digipymon)
            self.cantidad_digipymon += 1
        else:
            print("No se puede añadir más Digipymons. Se ha alcanzado el límite de 6.")
            return

    def consultar_digicoins(self):
        print("Digicoins de", self.nombre, ":", self.digicoins)

    def añadir_objeto_al_inventario(self, nombre_objeto, cantidad):
        # Añadir objeto al inventario, aumentando la cantidad si ya existe
        if nombre_objeto in self.inventario:
            self.inventario[nombre_objeto] += cantidad
        else:
            self.inventario[nombre_objeto] = cantidad