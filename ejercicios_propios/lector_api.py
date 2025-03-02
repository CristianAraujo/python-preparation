# Date: March 01, 2025

"""
32. Usar requests para hacer peticiones HTTP
Crea un script que haga una petición HTTP a 
una API pública y muestre la respuesta en formato JSON.
"""

import requests
import json

url = 'http://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url)
datos_json = response.json()

print(json.dumps(datos_json, indent=4))