from modelos.Producto import Producto
from modelos.Cliente import Cliente
from servicios.Restaurante import Restaurante

# Crear el restaurante
restaurante = Restaurante("Restaurante Sabor Amazónico")

# Crear productos
producto1 = Producto("Hamburguesa", 5.50, "Comida", True)
producto2 = Producto("Pizza", 8.00, "Comida", True)
producto3 = Producto("Jugo Natural", 2.50, "Bebida", True)

# Crear clientes
cliente1 = Cliente("Arely Rivera", "1723456789", "0991234567", True)
cliente2 = Cliente("Juan Pérez", "1712345678", "0987654321", False)

# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print("========== RESTAURANTE ==========")
print(restaurante.nombre)

restaurante.mostrar_productos()
restaurante.mostrar_clientes()

# Ejecutar algunos métodos
cliente1.pedir()
producto2.actualizar_precio(9.00)

print("\n=== PRODUCTOS ACTUALIZADOS ===")
restaurante.mostrar_productos()