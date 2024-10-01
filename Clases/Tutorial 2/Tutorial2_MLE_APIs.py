# -*- coding: utf-8 -*-
"""Tutorial2_BigData_APIs.ipynb

# Tutorial - Machine Learning para Economistas
## Tutorial 2

- Conocer qué son y cómo trabajar con APIs

¿Qué es una API? Los sistemas tienen distintos tipos de interfaces que permiten interactuar con ellos.

* **GUI (Graphical User Interface o interfaz gráfica)**: El usuario clickea e interactúa con distintos objetos para ejecutar acciones y lograr sus objetivos. Las páginas web tienen interfaces gráficas.
* **API (Application Programming Interface o interfaz de programación)**: El usuario escribe líneas de código para interactuar con el sistema, ejecutar acciones y lograr sus objetivos.

Todos los sitios web tienen una interfaz gráfica con la que estamos acostumbrados a interactuar, y también tienen una interfaz de programación más o menos desarrollada, o más o menos expuesta, con la cual tal vez no estemos tan acostumbrados a interactuar.

Ejemplo:

En https://www.mercadolibre.com.ar/ podemos buscar en el buscador "pelotas", apretar "Enter" y el sistema devuelve el resultado de una búsqueda. Si, en cambio, ponemos por "pelotas futbol" y apretamos "Enter" de nuevo, cambiará el resultado de la búsqueda. Esta es la **interfaz gráfica del sitio**.

Sin embargo, también podríamos lograr el mismo objetivo sólo escribiendo distintas URLs en el navegador:

* https://listado.mercadolibre.com.ar/pelotas
* https://listado.mercadolibre.com.ar/pelotas-futbol

Esto es más parecido a lo que llamaríamos una **interfaz de programación**.

Las APIs son mecanismos que permiten que una aplicación o servicio acceda a un recurso en otra aplicación o servicio (un cliente accede a recurso en un servidor).

En la web, las interfaces de programación de uso más difundido son las APIs REST ([Representational state transfer](https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional)). REST es un estilo para diseñar aplicaciones que especifica un conjunto de protocolos y métodos para interactuar con los recursos de internet escribiendo líneas de código.

Estas APIs se comunican mediante el protocolo HTTP para interactuar con los recursos (es el medio de comunicación comunicación entre el usuario y el servidor). HTTP es el mismo protocolo que se utiliza para cargar páginas web en un navegador.
Este protocolo indica cómo estructurar un mensaje de texto que describa la petición (**request**) del usuario o cliente a un servidor. Hay distintos tipos de peticiones que un usuario puede realizar, algunas de ellas son:

* **POST**: Envía datos al servidor para crear un recurso nuevo.
* **GET**: Se utiliza para obtener información de un recurso alojado en el servidor.
* **PUT**: Actualiza (crea o modifica) un recurso del servidor.
* **DELETE**: Elimina un recurso del servidor.

El cliente manda una petición (**request**) y el servidor devuelve una respuesta (**response**).

Fuente: Curso de Instituto Humai - APIs

Cada vez que vamos al navegador y escribimos la dirección de una página web, **estamos haciendo un GET request** a un servidor. Esto es una petición para adquirir el código de un recurso que queremos visualizar en el navegador.

La URL es la parte más importante de la definición de un GET request (aunque el navegador agrega otras cosas también, que no vemos) y nos permite cambiar la representación deseada de un mismo recurso de distintas maneras:

* https://deportes.mercadolibre.com.ar/pelotas-futbol pide al servidor pelotas de fútbol.
* https://deportes.mercadolibre.com.ar/pelotas-futbol_OrderId_PRICE pide al servidor pelotas de fútbol ordenadas por precio.

Cuando escribimos una URL en un navegador, la mayoría de las veces hacemos GET requests que devuelven código HTML (el código que da una estructura a una página web, tal como vimos en el video anterior cuando obteníamos el código HTML al hacer web scraping). Pero los GET requests pueden devolver datos en otros formatos (por ejemplo en JSON y en CSV).

Las APIs REST que definen GET requests capaces de devolver datos en formato JSON y CSV, son particularmente útiles cuando queremos analizar datos.

Ahora vamos a conocer algunas APIs.

### Vamos a usar la API de Mercado Libre

En particular, vamos a:
- ver los resultados de una búsqueda
- obtener la descripción de una publicación

Para ver más información ir a: https://developers.mercadolibre.com.ar/
"""

import requests

"""#### Obtener ítems de una consulta de búsqueda

- https://developers.mercadolibre.com.ar/es_ar/items-y-busquedas

Con el parámetro “q” puedes realizar una búsqueda por palabra, frases o tributos claves de búsqueda. Es importante tener en cuenta que en este campo puedes enviar tantos detalles de los atributos de la publicación como sea necesario, de esta manera en la respuesta obtendrás búsquedas más precisas. Si quieres separar términos puedes usar %20 que corresponde al código ASCII.

![meli_items.JPG](attachment:meli_items.JPG)

"""

# Así se ve la búsqueda en el navegador:
# https://listado.mercadolibre.com.ar/libro-introduction-to-statistical-learning

# Al usar la API tenemos que seguir este formato:
# https://api.mercadolibre.com/sites/$SITE_ID/search?q=nombre%20item

# Notar que:
# $SITE_ID: MLA  # MLA es el sitio de Argentina
# item: item a buscar. (reemplazamos los espacios con %20)

buscar = "libro introduction to statistical learning"
url = "https://api.mercadolibre.com/sites/{}/search?q={}".format("MLA", buscar.replace(" ", "%20"))

# Hacemos el pedido o request y obtenemos la response
response = requests.request("GET", url)
print(response) # correcto

# Vemos el texto
response.text

url

# Pero podríamos guardar el resultado en un diccionario (json)
data = response.json()
#type(data) # dict
data

# Ahora podemos acceder a los distintos resultados (usando las keys del diccionario), por ejemplo:

# Vemos la longitud de la lista de resultados
print('Longitud de lista de resultados:', len(data['results']))

# Vemos el precio del primer resultado de la búsqueda
print('Precio del primer resultado:', data['results'][0]['price'])

# Link del primer resultado
print(data['results'][0]['permalink'])

"""#### Consultar descripción de un ítem

- https://developers.mercadolibre.com.ar/en_us/item-description-2

"""

# Al usar la API tenemos que seguir este formato:
#https://api.mercadolibre.com/items/$ITEM_ID/description

# Veamos un ejemplo con el primer item que aparece al buscar el libro
print(data['results'][0]['id'])
print(data['results'][0]['permalink'])
#https://articulo.mercadolibre.com.ar/MLA-1121313969-book-introduction-to-statistical-and-machine-learning-_JM#position=3&search_layout=stack&type=item&tracking_id=05f493fb-55d2-468b-896f-8a1890e10e65v
# Vemos que
# $ITEM_ID es MLA1675597856 # no se pone el guion medio

url = "https://api.mercadolibre.com/items/{}{}/description".format("MLA", '1675597856')
response2 = requests.get(url)
response2.text

"""### API Series de Tiempo

La **[API Series de Tiempo de la Republica Argentina](https://apis.datos.gob.ar/series)** es una API REST desarrollada y mantenida por el Estado Nacional de Argentina para la consulta de estadísticas en formato de series de tiempo. Contiene series publicadas por organismos de la Administración Pública Nacional.

La API permite:

* [Buscar series](https://datosgobar.github.io/series-tiempo-ar-api/reference/search-reference/) por texto. También se pueden buscar en el sitio web de datos.gob.ar: https://datos.gob.ar/series
* Cambiar la frecuencia (por ejemplo: convertir series diarias en mensuales)
* Elegir la función de agregacion de valores, usada en el cambio de frecuencia (una serie se puede convertir de diaria a mensual promediando, sumando, sacando el maximo, el minimo, el ultimo valor del periodo, etc)
* Filtrar por rango de fechas
* Elegir el formato (CSV o JSON)
* Cambiar configuracion del CSV (caracter separador, caracter decimal)

En https://datos.gob.ar/series podés buscar series de tiempo publicadas por distintos organismos de la Administración Pública Nacional en Argentina y usar el link al CSV para leerlos directamente desde python con pandas.

También podes **buscar los ids de las series de interés** y juntarlos en la misma consulta para armar una tabla de hasta 40 series.
"""

# Un ejemplo



url_arg = "https://apis.datos.gob.ar/series/api/series?ids=102.1_I2NG_ABRI_M_22,101.1_I2NG_2016_M_22&format=json"

response = requests.get(url_arg)
print(response)

datos = response.json()
datos

