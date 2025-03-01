from collections import Counter

def sugerir_productos(productos, compras_usuario):
    # Crear un diccionario de productos con sus categorías
    categoria_por_producto = {nombre: categoria for nombre, categoria in productos}
    
    # Contar la cantidad de compras por categoría
    conteo_categorias = Counter(categoria_por_producto[producto] for producto in compras_usuario if producto in categoria_por_producto)
    
    if not conteo_categorias:
        return []  # Si el usuario no ha comprado nada, no hay sugerencias
    
    # Encontrar la categoría más comprada (o categorías en caso de empate)
    max_compras = max(conteo_categorias.values())
    categorias_mas_compradas = {cat for cat, count in conteo_categorias.items() if count == max_compras}
    
    # Filtrar productos que pertenecen a las categorías más compradas y que aún no ha comprado
    productos_sugeridos = [nombre for nombre, categoria in productos if categoria in categorias_mas_compradas and nombre not in compras_usuario]
    
    # Ordenar alfabéticamente
    return sorted(productos_sugeridos)

# Ejemplo de uso
productos = [
    ("Laptop", "Electrónica"), ("Teléfono", "Electrónica"), 
    ("Teclado", "Accesorios"), ("Mouse", "Accesorios"), 
    ("Cámara", "Fotografía"), ("Lente", "Fotografía")
]

compras_usuario = ["Laptop", "Teléfono", "Teclado"]

print(sugerir_productos(productos, compras_usuario))  # Salida esperada: ["Mouse"]
