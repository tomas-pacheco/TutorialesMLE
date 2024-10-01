"""

# Tutorial de Big Data
## Tutorial 2

El objetivo de esta clase es ver cómo extraer datos de internet por medio de Web Scraping y cómo interactuar con una APIs. También veremos una introducción a los métodos de sentiment analysis.

- Web Scraping
- APIs
- Sentiment analysis

### Web Scraping: extrayendo datos de internet

#### ¿Qué es web scraping?

La práctica de recopilar datos a través de cualquier medio que no sea un programa que interactúa con una API o un humano que usa un navegador web. En general esto se logra mediante un programa automatizado que consulta un servidor web, solicita datos (generalmente en forma de HTML y otros archivos que componen las páginas web) y luego analiza esos datos para extraer la información necesaria.

Fuente: Ryan Mitchell (2015). Web Scraping with Python.

#### Antes de empezar

###### Aspectos éticos y legales del web scraping
Web scraping es la extracción de datos de sitios web, es una forma automática de guardar información que se presenta en nuestro navegador (muy usada tanto en la industria como en la academia). Sus aspectos legales dependerán de cada sitio. Respecto a la ética es importante que nos detengamos a pensar si estamos o no generando algun perjuicio.

###### No reinventar la rueda
Emprender un proyecto de web scraping a veces es rápido y sencillo, pero en general requiere tiempo y esfuerzo. Siempre es aconsejable asegurarse de que valga la pena y antes iniciar hacerse algunas preguntas:
* ¿La informacion que necesito ya se encuentra disponible? (ej: APIs)
* ¿Vale la pena automatizarlo o es algo que lleva poco trabajo a mano?

#### Conceptos básicos sobre la web

HTML, CSS y JavaScript son los tres lenguajes principales con los que está hecho la parte de la web que vemos (*front-end*).

Una analogía para entender cómo funcionan:
- HTML como la estructura de la casa.
- CSS como la decoración interior y exterior.
- JavaScript como el sistema eléctrico, del agua y otras funcionalidades que hacen una casa habitable

Si quieren ver más cómo se unen HTML+CSS+Javascript: https://codepen.io/voubina/pen/gOZGPYx

Fuente de las imágenes:
https://geekflare.com/es/css-formatting-optimization-tools/ <br>
https://www.nicepng.com/ourpic/u2q8i1o0e6q8r5t4_html5-css3-js-html-css-javascript/

Fuente de la información: Instituto Humai - Curso de Automatización

##### HTML

- HTML quiere decir: lenguaje de marcado de hipertexto o HyperText Markup Language por sus siglas en inglés.
- El código  HTML da estructura a los sitios web.
- El código HTML se conforma por distintos elementos que le dicen al navegador cómo mostrar el contenido.
- Esos elementos son etiquetas. Hay etiquetas para indicar qué contenido es un título, un párrafo, un enlace, una imagen, etc.

|Etiqueta (Tag)     |Descripción|
|:--------|:--------|
|`<!DOCTYPE>`  | 	Define el tipo de documento|
|`<html>`      |	Define un documento HTML |
|`<head>`      |	Contiene metadata/información del documento|
|`<title>`     |	Define el título del documento|
|`<body>`      |	Define el cuerpo del documento|
|`<h1>` a `<h6>`|	Define títulos |
|`<p>`         |	Define un párrafo|
|`<br>`        |	Inserta un salto de línea (line break) |
|`<!--...-->`	 |  Define un comentario|
    
Para saber más sobre HTML podés consultar [acá](https://www.w3schools.com/TAGS/ref_byfunc.asp) la lista de etiquetas de este lenguaje.

###### ¿Cómo consigo el código HTML?

Ahora que sabemos cuál es el componente principal de los sitios webs podemos intentar programar a nuestra computadora para leer HTML y extraer información útil.

Para conseguir el código de un sitio web podemos:
- Ir a herramientas del desarrollador (`ctrl+shift+i`) en el navegador.
- Presionar `ctrl+u` en el navegador.

Para hacer lo mismo desde Python podemos usar la librería requests (vamos a verlo ahora)

### Primer ejemplo: títulos de noticias

#### **Método: BeautifulSoup**
* Esta librería provee un *parser* de html, o sea un programa que analiza/entiende el código. Así, nos permite hacer consultas más sofisticadas de forma simple, por ejemplo: "buscar todos los títulos h2 del sitio".

* Se usa para extraer los datos de archivos HTML. Crea un árbol de análisis a partir del código fuente de la página que se puede utilizar para extraer datos de forma jerárquica y más legible.

Empecemos!
"""

#pip install requests
#pip install BeautifulSoup
#pip install pandas
# Nota: si no tienen instaladas las librarías a importar debajo, primero deben instalarlas
# (para eso, quiten el # y activen las 3 líneas de código de arriba)

import requests #html requestor
from bs4 import BeautifulSoup #html parser
import pandas as pd #dataframe manipulator

url = "https://www.lanacion.com.ar/"

r = requests.get(url) #traigo el contenido del html
contenido = r.content

soup = BeautifulSoup(contenido, "html.parser")
soup

"""Seleccionando un título que aparece bajo la etiqueta o tag h2, vemos, por ejemplo:
Nota: esto cambia según el día en que hagan el request o pedido (ya que la página de noticias se actualiza)

<h2 class="text ln-text title --prumo --font-medium --font-m-l"><span class="text ln-text lead --prumo --font-extra">Tras la reunión.<!-- --> </span>Un gobernador reveló el piso de Ganancias y la fórmula jubilatoria que propone el Gobierno</h2>

### Opción A - Usando find y find_all
"""

# Dentro de la sopa, busco los elementos que contienen la información que necesito
# Buscamos el elemento <h2> indicando la clase (class). Escribo class_ porque "class" es una palabra reservada en Python
h2_element = soup.find('h2', class_='text ln-text title --prumo --font-medium --font-m-l')

# Obtenemos el texto del elemento <h2>
h2_text = h2_element.text.strip()  # strip() permite remover espacios sobrantes

print(h2_element)
print('\n', h2_text)

# Obtuvimos el *primer* elemento de la página con ese tag. Pero queremos hacerlo para todos los títulos...
# El método "find_all" busca TODOS los elementos de la página con ese tag y devuelve una lista que los contiene
# (en realidad devuelve un objeto de la clase "bs4.element.ResultSet")
h2_elements = soup.find_all('h2')

print(type(h2_elements))
print('\n', h2_elements)

# Extraemos el texto de cada elemento <h2> e imprimimos
for h2_element in h2_elements:
    h2_text = h2_element.text.strip()
    print(h2_text)
    print(" ")

# Aclaración: el nombre del ítem por el que iteramos puede ser el que nosotros queramos, por ejemplo: i
for i in h2_elements:
    h2_text = i.text.strip()
    print(h2_text)

# Idealmente, tenemos que guardar estos títulos, queremos analizarlos
titulos = [] # primero creamos una lista

# Extraemos el texto de cada elemento <h2> y ahora guardamos
for h2_element in h2_elements:
    h2_text = h2_element.text.strip()
    #print(h2_text)

    titulos.append({
        'titular': h2_text
    })

# Creamos un dataframe a partir de la lista de títulos
titulos_df = pd.DataFrame(titulos)

titulos_df

"""### Opción B - Usando select. Defino un selector

Un selector es un descriptor de un elemento de HTML. Como antes usamos la etiqueta (tag) h2 para encontrar los elementos buscados, un selector combina etiquetas, clases y ids en un solo string para hacer la búsqueda deseada.

Si quieren [acá](https://www.w3schools.com/cssref/css_selectors.php) tienen un enlace para leer más sobre selectores
"""

# Definimos un selector de los objetos que englobe la información buscada
# Vamos a tratar de ser más precisos: vimos que los títulos están bajo los tags h2, pero ahora
# buscaremos indicar en qué objeto se encontraban estos tags h2
# (y así indicar dónde encontrar los h2 con más precisión)

# En este caso los titulares se encuentran en diferentes "description containers"
desc_selector = '.description-container'; # Identifica todos los elementos HTML con la clase 'description container'.
# Nota: Antes de la clase se pone un punto

# Con el método select y el selector especificado buscamos todos los elementos deseados
desc_elements = soup.select(desc_selector) # Nuevamente, obtenemos un "bs4.element.ResultSet"

print(type(desc_elements)) # bs4.element.ResultSet
print('\n Primer elemento de los resultados:\n', desc_elements[0])
print('\n', type(desc_elements[0])) # bs4.element.Tag

# Una vez obtenidas ya las cajas con los titulares, buscamos los elementos dentro de cada una que contengan los títulos
# Definimos un selector de estos elementos
h2_selector = 'h2' # Identifica todos los elementos HTML cuyo tag sea 'h2'

print(desc_elements[1])
print('\n', desc_elements[1].select(h2_selector))

# Creamos una lista vacía para guardar los títulos
titulos_sel = []

# Realizamos un loop por todas las descripciones encontradas. Y por cada una, ejecutamos una consulta local
# a cada elemento, buscando entonces el título de cada noticia con el selector ya definido
for desc in desc_elements :
    # Nos quedamos con el 1er resultado, ya que asumimos que nuestro selector es suficientemente preciso
    # como para encontrar solo resultados válidos.
    h2_element = desc.select(h2_selector)[0]
    titular = h2_element.get_text() # Obtenemos el texto

    titulos_sel.append({
        'titular': titular
    })

# Creamos un dataframe con los títulos a partir de la lista
titulos_sel_df = pd.DataFrame(titulos_sel)

titulos_sel_df


"""### Análisis de sentimiento de los títulos de noticias

Más información sobre sentiment analysis, acá: https://www.datacamp.com/tutorial/text-analytics-beginners-nltk

"""

# Si aún no instalaron estas librerías, activar estas líneas de código -quitar #- para instalarlas
#pip install string
#pip install pandas
#pip install nltk
#pip install stop_words
#pip install spacy
#!python -m spacy download es_core_news_sm
#pip uninstall vaderSentiment
#pip install vader-multi

# Importamos los paquetes a utilizar
import string
import pandas as pd
import nltk # para procesamiento del lenguaje natural
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.stem import WordNetLemmatizer
import spacy # para preprocesamiento en español
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# ntlk requiere descargar algunos datos adicionales
#nltk.download('all')

# Para trabajar en inglés usar:
from textblob import TextBlob

"""Vamos a limpiar los títulos
Como parte del preprocesamiento de la información tenemos los siguientes pasos:
1. Tokenization: Implica dividir el texto en palabras (o tokens)
2. Eliminar stop words: quitar palabras comunes e irrelevantes que no tienen mucho "sentimiento". Esto permite mejorar la precisión del análisis de sentimiento
3. Lemmatization: reducir las palabras a sus raíces (por ejemplo, eliminando sufijos, pasar de "leyendo" a "leer").
"""

# Veamos la lista de signos de puntuación
print(string.punctuation)
# Como estamos trabajando en español, es conveniente agregar algunos símbolos más a los signos de puntuación
string.punctuation = string.punctuation + '¿¡“”'
print(string.punctuation)

# Cargar palabras vacías en español
stop_words = get_stop_words('spanish')
print(stop_words)

def limpiar_titulos_nltk(titulo):
    '''
    Esta función limpia el texto del título.
    Convierte texto en tokens, elimina stop words, y transforma palabras en su forma raíz
    para dejar en el texto solo las palabras con mayor contenido.
    Input:
        título (str): Texto del título original
    Output:
        título (str): Texto del título limpio
    '''

    # 1. Separar los títulos en tokens (obtenemos una lista con palabras)
    word_tokens = word_tokenize(titulo.lower())

    # 2. Eliminar palabras vacías (stop words) de los títulos
    # Loop por las condiciones
    filtered_tokens = []
    for w in word_tokens:
        # Verificamos tokens contra stop words y puntuación
        if w not in stop_words and w not in string.punctuation:
            filtered_tokens.append(w)

    # 3. Lemmatization
    lemmatizer = WordNetLemmatizer()

    lemmatized_tokens = []
    for w in filtered_tokens:
        lemmatizer.lemmatize(w)
        lemmatized_tokens.append(w)

    # Volvemos a armar la oración (concatenamos las palabras separándolas con un espacio)
    return ' '.join(lemmatized_tokens)

# Cargar el modelo para el español y las stop words según spacy
nlp = spacy.load('es_core_news_sm')
stopwords_spacy = spacy.lang.es.stop_words.STOP_WORDS

def limpiar_titulos_spacy(titulo):
    '''
    Esta función limpia el texto del título (usando funcionalidades de la librería spacy).
    Convierte texto en tokens, elimina stop words, y transforma palabras en su forma raíz
    para dejar en el texto solo las palabras con mayor contenido.
    Input:
        título (str): Texto del título original
    Output:
        título (str): Texto del título limpio
    '''

    # Procesar el texto con spaCy
    doc = nlp(titulo.lower())
    #print(doc)

    filtered_tokens = []
    lemmas = []

    # Pasar a tokens y eliminar puntación y stopwords
    for w in doc:
        if w.text not in stopwords_spacy and not w.is_punct:
            filtered_tokens.append(w.text)
    filtered_doc = ' '.join(filtered_tokens)
    #print(filtered_doc)

    # Obtener las formas lematizadas de las palabras
    doc2 = nlp(filtered_doc)
    for w_f in doc2:
        lemmas.append(w_f.lemma_)

    # Volvemos a armar la oración (concatenamos las palabras separándolas con un espacio)
    return ' '.join(lemmas)

#Este es un título sucio:
titulos_sel[0]

#Este es un título limpio:
limpiar_titulos_nltk(titulos_sel[0]['titular'])

#Este es un título limpio:
limpiar_titulos_spacy(titulos_sel[0]['titular'])

"""#### Ahora vamos a usar sentiment analysis para ver qué tan positivos son los títulos

Vamos a usar la bilioteca NLTK (Natural Language Toolkit) para clasificar los títulos en positivos o negativos. NLTK es una biblioteca de Python muy utilizada en procesamiento de lenguaje natural (NLP). VADER (Valence Aware Dictionary and Sentiment Reasoner) es un módulo específico de NLTK que se utiliza para el análisis de sentimientos.

VADER es una herramienta especialmente diseñada para el análisis de sentimientos en textos. A diferencia de algunos enfoques más generales que utilizan modelos de aprendizaje automático, VADER se basa en un conjunto de reglas y un diccionario que asigna puntuaciones de polaridad a palabras y expresiones. Además, tiene en cuenta factores como las mayúsculas, los signos de puntuación y los emoticonos para evaluar la intensidad del sentimiento.

Las puntuaciones de VADER incluyen la polaridad (positiva, negativa o neutra) y una medida de la intensidad del sentimiento. Es especialmente útil para textos informales o con lenguaje coloquial, como se encuentra comúnmente en redes sociales.

Vamos a probar dos módulos con VADER:
1. con VADER "original". Ver: https://www.nltk.org/_modules/nltk/sentiment/vader.html
2. con VADER "multi". Ver: https://github.com/brunneis/vader-multi
En realidad, ambos buscan hacer los mismo pero los modelos de fondo están entrenados de formas distintas
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Inicializar el analizador de sentimientos VADER
sia = SentimentIntensityAnalyzer()

# Primero veamos un ejemplo
texto_ej_pos = "Me encanta este curso, es genial"
texto_ej_neg = "Odio este curso, es terrible"
texto_ej_neu = "Me da igual el curso"

print(texto_ej_pos, sia.polarity_scores(texto_ej_pos))
print(texto_ej_neg, sia.polarity_scores(texto_ej_neg))
print(texto_ej_neu, sia.polarity_scores(texto_ej_neu))
# Si la variable compound es positiva, el texto es positivo; si es negativa, el texto es negativo
# Y si se encuentra en el rango del 0 es un mensaje neutro

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SentimentIntensityAnalyzerMulti

# Inicializar el analizador de sentimientos VADER
sia2 = SentimentIntensityAnalyzerMulti()

# Primero veamos un ejemplo
texto_ej_pos = "Me encanta este curso, es genial"
texto_ej_neg = "Odio este curso, es terrible"
texto_ej_neu = "Me da igual el curso"

print(texto_ej_pos, sia2.polarity_scores(texto_ej_pos))
print(texto_ej_neg, sia2.polarity_scores(texto_ej_neg))
print(texto_ej_neu, sia2.polarity_scores(texto_ej_neu))
# Si la variable compound es positiva, el texto es positivo; si es negativa, el texto es negativo
# Y si se encuentra en el rango del 0 es un mensaje neutro

"""Ahora crearemos funciones que, además de dar un valor, clasifiquen en positivo, negativo o neutro"""

def analizar_sentiment(text):
    # Obtener la polaridad del sentimiento
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)

    # Clasificar el sentimiento como positivo, negativo o neutro
    compound_score = sentiment_score['compound']
    if compound_score >= 0.05:
        sentiment = "Positivo"
    elif compound_score <= -0.05:
        sentiment = "Negativo"
    else:
        sentiment = "Neutro"

    return compound_score, sentiment

def analizar_sentiment2(text):
    # Obtener la polaridad del sentimiento
    sia2 = SentimentIntensityAnalyzerMulti()
    sentiment_score = sia2.polarity_scores(text)

    # Clasificar el sentimiento como positivo, negativo o neutro
    compound_score = sentiment_score['compound']
    if compound_score >= 0.05:
        sentiment = "Positivo"
    elif compound_score <= -0.05:
        sentiment = "Negativo"
    else:
        sentiment = "Neutro"

    return compound_score, sentiment

# Ejemplos de uso
compound_score_pos, sentiment_pos = analizar_sentiment(texto_ej_pos)
print(f"Texto: {texto_ej_pos}")
print(f"Puntuación de sentimiento compuesta: {compound_score_pos}")
print(f"Sentimiento: {sentiment_pos}")

compound_score_neg, sentiment_neg = analizar_sentiment(texto_ej_neg)
print(f"\nTexto: {texto_ej_neg}")
print(f"Puntuación de sentimiento compuesta: {compound_score_neg}")
print(f"Sentimiento: {sentiment_neg}")

# Ejemplos de uso
compound_score_pos, sentiment_pos = analizar_sentiment2(texto_ej_pos)
print(f"Texto: {texto_ej_pos}")
print(f"Puntuación de sentimiento compuesta: {compound_score_pos}")
print(f"Sentimiento: {sentiment_pos}")

compound_score_neg, sentiment_neg = analizar_sentiment2(texto_ej_neg)
print(f"\nTexto: {texto_ej_neg}")
print(f"Puntuación de sentimiento compuesta: {compound_score_neg}")
print(f"Sentimiento: {sentiment_neg}")

# Ahora un ejemplo con un título limpio
print(titulos_sel[0]['titular'],
      "\n",
      analizar_sentiment(limpiar_titulos_spacy(titulos_sel[0]['titular'])))

# Aplicamos la función para limpiar títulos para tener un columna con títulos limpios
titulos_sel_df['titular_limpio'] = titulos_sel_df['titular'].apply(limpiar_titulos_nltk)
# Vemos el sentiment
titulos_sel_df['sentiment'] = titulos_sel_df['titular_limpio'].apply(analizar_sentiment)
titulos_sel_df['sentiment2'] = titulos_sel_df['titular_limpio'].apply(analizar_sentiment2)

titulos_sel_df

titulos_sel_df['sentiment'].value_counts()

titulos_sel_df['sentiment2'].value_counts()

titulos_sel_df.to_excel('titulos.xlsx', index=False)

"""#### Un ejemplo en inglés usando TextBlob"""

from textblob import TextBlob

# Ejemplo de texto en inglés
texto_ej_1 = "I love learning about Big data"
texto_ej_2 = "I hate learning about Big data"

# Crear un objeto TextBlob con el texto
blob1 = TextBlob(texto_ej_1)

# Obtener la polaridad del sentimiento (-1 a 1)
polarity1 = blob1.sentiment.polarity

# Clasificar el sentimiento como positivo, negativo o neutro
def clasif_polarity(polarity):
    if polarity > 0:
        sentiment = "Positivo"
    elif polarity < 0:
        sentiment = "Negativo"
    else:
        sentiment = "Neutro"
    return sentiment

# Mostrar los resultados
print(f"Texto: {texto_ej_1}")
print(f"Polaridad del sentimiento: {polarity1}")
print(f"Sentimiento: {clasif_polarity(polarity1)}")

"""### Otro Ejemplo de Web Scraping: Tabla"""

import requests #html requestor
from bs4 import BeautifulSoup #html parser
import pandas as pd #dataframe manipulator

url = 'https://datatables.net/examples/basic_init/zero_configuration.html'

"""Solicitamos el html del url indicado. El código de respuesta 200 significa que la respuesta del sitio fue exitosa"""

response = requests.get(url)
print(response.status_code)

"""Dividimos el texto con `BeautifulSoup`."""

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

"""Se puede observar que la informacion que queremos extraer esta entre las etiquetas llamadas `tr`. Por lo tanto queremos encontrar todas las etiquetas `tr`."""

info = soup.find_all('tr')
info

print(type(info))
print(type(info[0]))

"""Podemos ver que todas las observaciones, excepto la primera y la última, contienen la información que necesitamos. También observamos que el nombre, el puesto, el cargo, la edad, la fecha de inicio y el salario siempre tienen el mismo orden. Podemos hacer uso de estos patrones para extraer la información en un marco de datos."""

df = pd.DataFrame(columns=['name', 'position', 'office', 'age', 'start date', 'salary'])

print(info[1].find_all('td'))

for i, item in enumerate(info): #enumerate da la posición
    if i != 0 and i != len(info)-1:
        datos_de_fila = item.find_all('td')
        fila = []
        for dato in datos_de_fila:
            fila.append(dato.text)
        print('\nFila:', i)
        print(fila)
        df.loc[i-1] = fila # mencionamos el nombre/etiqueta de las filas que queremos seleccionar

display(df)

"""Por último exportamos la información a un archivo `csv`:"""

df.to_csv('final_output.csv', index=False)





