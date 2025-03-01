from collections import Counter

def sugerir_productos(productos, compras_usuario):
    # Crear un diccionario de productos con sus categorías
    categoria_por_producto = {nombre: categoria for nombre, categoria in productos}
    
    # Contar la cantidad de compras por categoría
    conteo_categorias = Counter(categoria_por_producto[producto] for producto in compras_usuario if producto in categoria_por_producto)
    
    if not conteo_categorias:
        return []  # Si el usuario no ha comprado nada, no hay sugerencias
    
    # Ordenar categorías por cantidad de compras (de mayor a menor)
    categorias_ordenadas = sorted(conteo_categorias.items(), key=lambda x: x[1], reverse=True)
    
    # Seleccionar la categoría más comprada
    categorias_mas_compradas = {categorias_ordenadas[0][0]}  # Primera categoría más comprada
    
    # Si hay más de una categoría y la segunda también tiene un número alto de compras, incluirla
    if len(categorias_ordenadas) > 1:
        categorias_mas_compradas.add(categorias_ordenadas[1][0])
    
    # Filtrar productos que pertenecen a las categorías seleccionadas y que el usuario no ha comprado
    productos_sugeridos = [nombre for nombre, categoria in productos if categoria in categorias_mas_compradas and nombre not in compras_usuario]
    
    # Si no hay sugerencias en las categorías más compradas, sugerir productos de cualquier otra categoría
    if not productos_sugeridos:
        productos_sugeridos = [nombre for nombre, categoria in productos if nombre not in compras_usuario]
    
    # Ordenar alfabéticamente
    return sorted(productos_sugeridos)

# Ejemplo de uso
productos = [
    ("Laptop", "Electrónica"), ("Teléfono", "Electrónica"), 
    ("Teclado", "Accesorios"), ("Mouse", "Accesorios"), 
    ("Cámara", "Fotografía"), ("Lente", "Fotografía")
]

compras_usuario = ["Laptop", "Teléfono", "Teclado"]

print(sugerir_productos(productos, compras_usuario))  
# Salida esperada: ["Mouse"] (porque Accesorios es la siguiente categoría con más compras)