class Cliente:
    def __init__(self, nombre, cedula, telefono, afiliado):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.afiliado = afiliado

    def pedir(self):
        print(f"{self.nombre} realizó un pedido.")

    def afiliarse(self):
        self.afiliado = True

    def __str__(self):
        return f"Cliente: {self.nombre} | Cédula: {self.cedula} | Teléfono: {self.telefono} | Afiliado: {self.afiliado}"