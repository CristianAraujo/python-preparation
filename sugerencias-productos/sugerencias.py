# Date: February 28, 2025

from collections import Counter

# class Producto:
#     def __init__ (self, name, category):
#         self.name = name
#         self.category = category

def sugerencias(productos, compras_usuario):
    categoria_por_producto = { nombre: categoria for nombre, categoria in productos }
    print(f'categorias_por_producto: {categoria_por_producto}')

    conteo_categorias = Counter(categoria_por_producto[producto] for producto in compras_usuario)
    print(f'conteo_categorias: {conteo_categorias}')

    if not conteo_categorias: return []

    max_compras = max(conteo_categorias.values())
    print(f'max_compras: {max_compras}')

    categorias_mas_compradas = { cat for cat, count in conteo_categorias.items() if count == max_compras }
    print(f'categorias_mas_compradas: {categorias_mas_compradas}')

    productos_sugeridos = [
        nombre for nombre, categoria in productos 
        if categoria in categorias_mas_compradas and nombre not in compras_usuario 
    ]
    print(f'productos_sugeridos:{productos_sugeridos}')

    return sorted(productos_sugeridos)

if __name__ == '__main__':
    productos = [
        ("Laptop", "Electrónica"), 
        ("Teléfono", "Electrónica"), 
        ("Teclado", "Accesorios"), 
        ("Mouse", "Accesorios"), 
        ("Cámara", "Fotografía"), 
        ("Lente", "Fotografía")
    ]

    compras_usuario = ["Laptop", "Teléfono", "Teclado"]
    
    print(f'productos en main: {productos}')
    print(f'compras_usuario en main: {compras_usuario}')
    print(sugerencias(productos, compras_usuario))