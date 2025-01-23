class Inventario:
    def __init__(self):
        # Constructor por defecto con un diccionario vacío para almacenar objetos
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        # Comprobar si el objeto ya existe en el diccionario
        if nombre in self.objetos:
            # Si existe, añadir la cantidad al objeto existente
            self.objetos[nombre] += cantidad    
        else:
            # Si no existe, crear una nueva entrada en el diccionario
            self.objetos[nombre] = cantidad

    def usar_objeto(self, nombre, cantidad):
        # Disminuir la cantidad del objeto
        if nombre in self.objetos:
            self.objetos[nombre] -= cantidad
            # Si la cantidad llega a 0, eliminar el objeto del inventario
            if self.objetos[nombre] == 0:
                del self.objetos[nombre]
        else:
            print(f"El objeto '{nombre}' no está en el inventario.")
            
    def mostrar_inventario(self, label_resultado):
        if label_resultado is not None:
            if hasattr(self, 'objetos'):
                resultado = "Inventario:\n"
                for objeto, cantidad in self.objetos.items():
                    resultado += f"{objeto}: {cantidad}\n"
                label_resultado.config(text=resultado)
            else:
                label_resultado.config(text="Error: No se pudo acceder al inventario")
        else:
            print("Error: label_resultado no está bien definido.")