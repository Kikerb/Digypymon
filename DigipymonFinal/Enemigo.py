from Digipymon import Digi


class Enemigo(Digi):
    def __init__(self, nombre, vida, ataque, tipo, nivel):
        super().__init__(nombre, vida, ataque, tipo, nivel)
        self.lista_digipymon = []
        self.cantidad_digimon = 0

    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digimon += 1

    def __str__(self):
        stats_enemigo = [digi.__str__() for digi in self.lista_digipymon]
        stats_enemigo_str = "\n".join(stats_enemigo)
        return f"Enemigo: {self.nombre}\nCantidad de Digipymons: {self.cantidad_digimon}\n{stats_enemigo_str}"