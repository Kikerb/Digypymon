class Digi:
    def __init__(self, nombre, vida, ataque, tipo, nivel):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.vida_maxima = vida
         # Verificar si el tipo está entre los tipos válidos
        if tipo in ["Agua", "Fuego", "Planta"]:
            self.tipo = tipo
        else:
            # Si el tipo no es válido, establecerlo como "Desconocido"
            self.tipo = "Desconocido"
        self.nivel = nivel

    def curar(self):
        self.vida = self.vida_maxima  # Restaurar vida a su máximo

    def chetar(self):
        self.ataque *= 1.5 


    def __str__(self):
        return f"Digipymon: {self.nombre}\nVida: {self.vida}\nAtaque: {self.ataque}\nTipo: {self.tipo}\nNivel: {self.nivel}"