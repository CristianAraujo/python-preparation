import traceback

def function_a():
    1 / 0  # Esto causará un error de división por cero

def function_b():
    function_a()  # Llama a la función que causará el error

try:
    function_b()  # Llama a la función que hace todo el trabajo
except ZeroDivisionError as e:
    print(f"Excepción capturada: {e}")
    print("Imprimiendo el traceback:")
    traceback.print_tb(e.__traceback__)
    print("\nAccediendo a la traza detallada:")
    tb_list = traceback.extract_tb(e.__traceback__)  # Extrae información más detallada
    for tb in tb_list:
        print(f"Archivo: {tb.filename}, Línea: {tb.lineno}, Función: {tb.name}, Código: {tb.line}")
