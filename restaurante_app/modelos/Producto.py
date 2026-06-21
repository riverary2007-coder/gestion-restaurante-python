class Producto:
    def __init__(self, nombre, precio, categoria, disponible):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def cambiar_disponibilidad(self, estado):
        self.disponible = estado

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Categoría: {self.categoria} | Disponible: {self.disponible}"