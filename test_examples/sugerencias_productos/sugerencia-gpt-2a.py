from collections import Counter

def sugerencias(productos, compras_usuario):
    categoria_por_producto = {nombre: categoria for nombre, categoria in productos}
    print(f'categorias_por_producto: {categoria_por_producto}')

    conteo_categorias = Counter(categoria_por_producto[producto] for producto in compras_usuario if producto in categoria_por_producto)
    print(f'conteo_categorias: {conteo_categorias}')

    if not conteo_categorias:
        return []

    max_compras = max(conteo_categorias.values())
    print(f'max_compras: {max_compras}')

    # Ordenar categorías por número de compras
    categorias_ordenadas = sorted(conteo_categorias.items(), key=lambda x: x[1], reverse=True)
    print(f'categorias_ordenadas: {categorias_ordenadas}')

    # Obtener las categorías con el máximo y el segundo máximo
    categorias_mas_compradas = {categorias_ordenadas[0][0]}  # Primera categoría más comprada
    if len(categorias_ordenadas) > 1:
        categorias_mas_compradas.add(categorias_ordenadas[1][0])  # Segunda categoría más comprada

    print(f'categorias_mas_compradas: {categorias_mas_compradas}')

    productos_sugeridos = [
        nombre for nombre, categoria in productos 
        if categoria in categorias_mas_compradas and nombre not in compras_usuario
    ]
    print(f'productos_sugeridos: {productos_sugeridos}')

    return sorted(productos_sugeridos) if productos_sugeridos else ["No hay sugerencias"]

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