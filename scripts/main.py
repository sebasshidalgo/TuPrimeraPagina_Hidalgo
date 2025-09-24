# Script para probar la funcionalidad de las clases y métodos (corresponde a 2° Pre-Entrega)

# Importaciones
import uuid
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from TuPrimeraPagina_Hidalgo.clientes_app.logic.cliente import Cliente
from TuPrimeraPagina_Hidalgo.clientes_app.logic.cliente_corporativo import ClienteCorporativo
from TuPrimeraPagina_Hidalgo.clientes_app.logic.producto import Producto

# Crear instancias de clientes
cliente1 = Cliente("Juan", "Perez", "10456887", "Av. Corrientes 5040, CABA", "1134678342")
cliente2 = Cliente("Pedro", "Ramirez", "33233421", "Av. Santa Fe 3882, CABA", "1165148228")
cliente3 = Cliente("Maria", "García", "28756324", "Soler 3745, CABA", "1123435678")

# Crear un cliente corporativo
cliente_corp = ClienteCorporativo("Roberto", "González", "25987654", "Av. Libertador 4500, CABA", 
                               "1145678932", "30-71234567-8", "Empresa XYZ S.A.", "XYZ Tech")

print("=== INFORMACIÓN DE CLIENTES ===")
# Imprimir datos públicos de clientes mediante __str__
print(cliente1)
print(cliente2)
print(cliente3)
print(cliente_corp)
print("----------------------------------")

# Obtener info privada de clientes mediante getters
print(cliente1.get_documento())
print(cliente2.get_domicilio())
print(cliente3.get_telefono())
print(cliente_corp.get_cuit())
print("----------------------------------")

# Acceder a atributo de clase
print(f"El tipo de cliente es: {cliente2.tipo}")
print("----------------------------------")

# Modificar info privada de clientes mediante setters
cliente1.set_documento("33333333")
cliente2.set_domicilio("Calle Falsa 123, Springfield")
cliente3.set_telefono("1123456789")

# Imprimimos info modificada
print(cliente1.get_documento())
print(cliente2.get_domicilio())
print(cliente3.get_telefono())
print("----------------------------------")

# Crear productos
print("\n=== PRODUCTOS CREADOS ===")
producto1 = Producto("Smartphone Samsung A54", "Teléfono con 128GB almacenamiento", 250000, 10, "SMSA54", Producto.CATEGORIA_ELECTRONICA)
producto2 = Producto("Notebook Lenovo", "Laptop con i5 y 8GB RAM", 500000, 5, "NB-LEN-i5", Producto.CATEGORIA_ELECTRONICA)
producto3 = Producto("Zapatillas Nike", "Zapatillas deportivas talle 42", 80000, 20, "ZAP-NIKE-42", Producto.CATEGORIA_INDUMENTARIA)

# Mostrar info de los productos
print(producto1)
print(producto2)
print(producto3)
print("----------------------------------")

# Operaciones de compra y venta
print("\n=== OPERACIONES DE COMPRA Y VENTA ===")

# Cliente compra un producto
print("\n1. Cliente compra directamente:")
cliente1.comprar(producto1, 2)

# Producto se vende a un cliente
print("\n2. Producto se vende a un cliente:")
producto2.vender_a(cliente2, 1)

# Cliente corporativo compra un producto
print("\n3. Cliente corporativo realiza una compra:")
cliente_corp.comprar(producto3, 3)

# Consulta de stocks finales
print("\n=== VERIFICACIÓN DE STOCKS FINALES ===")
print(f"Stock de {producto1.nombre}: {producto1._Producto__stock} unidades")
print(f"Stock de {producto2.nombre}: {producto2._Producto__stock} unidades")
print(f"Stock de {producto3.nombre}: {producto3._Producto__stock} unidades")
print("----------------------------------")


