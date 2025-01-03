# import requests
# from bs4 import BeautifulSoup
# from ohllama import ia


# URL = 'https://www.gutenberg.org/cache/epub/29640/pg29640.txt'

# request = requests.get(URL)
# #devuelve un tipo String
# html = request.text

# #parsear HTML
# soup = BeautifulSoup(html, "html.parser")
# #por el momento no es necesario


# #llamamos a llama3.2
# inteligencia = ia()

# # post_ia = inteligencia.ia(pregunta=f'''Resume el texto a continuación, quita las partes que no tengan
# # nada que ver con el libro
# # aqui el texto:
# # {html}
# # ''')
# # print(post_ia)
            
from bs4 import BeautifulSoup
import requests

# URL de ejemplo que contiene una etiqueta <pre>
url = "https://www.gutenberg.org/cache/epub/29640/pg29640.txt"

# Hacer una solicitud a la URL
response = requests.get(url)

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Encontrar la primera etiqueta <pre> con los atributos específicos
pre_tag = soup.find('pre', attrs={'style': 'word-wrap: break-word; white-space: pre-wrap;'})

if pre_tag:
    # Obtener el contenido de la etiqueta <pre>
    contenido = pre_tag.text
    print("Contenido de la etiqueta <pre>:")
    print(contenido)
else:
    print("No se encontró ninguna etiqueta <pre> con los atributos especificados en la página.")
