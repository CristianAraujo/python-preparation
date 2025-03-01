# Date: March 01, 2025


"""
Prueba de sorted
"""
personas = {"Cristian": 35, "Maria": 71, "Carlos": 35, "Juan": 66}
personas_sorted_1 = sorted(personas, key=lambda x: x[0])
personas_sorted_2 = sorted(personas, key=lambda x: x[1])