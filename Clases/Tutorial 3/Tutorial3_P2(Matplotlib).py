# -*- coding: utf-8 -*-
"""

# Tutorial de Machine Learning para Economistas
## Tutorial 3 - Parte 2

El objetivo es graficar con matplotlib.

Matplotlib es la librería base de graficación, sobre la cual se montan otras librerías. Dentro de Matplotlib, usamos la dependencia "pyplot" que se instala con la librería. Por convención importamos así:
"""

#!pip install matplotlib
import matplotlib.pyplot as plt # importamos la librería gráfica. plt es el nombre por convención que se le asigna

"""Matplotlib genera los gráficos sobre dos objetos interrelacionados:
- **Figure**: la hoja en blanco, el recuadro que contiene hacia adentro el/los gráfico/s. En términos prácticos esto ocurre detrás de escenas, pero es lo que permite dibujar el gráfico.
- **Axes**: el gráfico en sí, los ejes y la informacíon graficada. La representación de la información sobre ejes.

Las partes de un gráfico
<img src="https://matplotlib.org/stable/_images/anatomy.png"
     width=500/>

Hay esencialmente dos maneras de graficar con Matplotlib:
- **Estilo pyplot**: simple y rápida para figuras que no son muy avanzadas. Quizás más fácil para empezar.
- **Estilo orientado-objetos**: un poco más complejo pero necesario para figuras que requieren mucha customización.

En cuanto al resultado estético, con ambos se puede lograr la misma calidad. Para dar los primeros pasos es indistinto cual se use. Sin embargo, el estilo orientado a objetos es necesario para figuras más complejas donde hay varios gráficos (subplots) y es necesario definir parámetros distintos para cada par de ejes (2D)

### Graficar con matplotlib
"""

import pandas as pd

import os
os.chdir("/Users/tomaspacheco/Library/CloudStorage/GoogleDrive-tpacheco@udesa.edu.ar/Mi unidad/UdeSA/MachineLearningEcon/Tutoriales/Tutorial 3/")

# Abrimos el archivo de potencia energética instalada en el país
df = pd.read_excel("potencia_instalada.xlsx")
# exploren la base

# Agregamos (collapse) a nivel de tipo de fuente
df_fuente = df.groupby(by=["periodo","fuente_generacion"]).agg({"potencia_instalada_mw":"sum"})
df_fuente.reset_index(inplace=True)
df_fuente.sample(5)

df_fuente.shape

"""Vamos a graficar dos líneas, así que definimos vector X e Y para cada una. Vamos a graficar la potencia instalada de generación por fuente Renovable y fuente Térmica:"""

# Definimos  vectores  de datos  para  serie 1 (renovable)
y1 = df_fuente[df_fuente["fuente_generacion"]=="Renovable"]["potencia_instalada_mw"]
x1 = df_fuente[df_fuente["fuente_generacion"]=="Renovable"]["periodo"]
# Definimos  vectores  de datos  para  serie 2 (térmica)
y2 = df_fuente[df_fuente["fuente_generacion"]=="Térmica"]["potencia_instalada_mw"]
x2 = df_fuente[df_fuente["fuente_generacion"]=="Térmica"]["periodo"]

# Nota: df[condicion][columna] selecciona la "columna" de la base que resulta de aplicar el filtro df[condicion].

# Creamos el gráfico al estilo pyplot

plt.plot(x1, y1, label="Renovable") # serie 1
plt.plot(x2, y2, label="Térmica") # serie 2
# Estas  dos  líneas  estaran  sobre  el mismo  gráfico

# Modifico  labels
plt.xlabel("Período")
plt.ylabel("Potencia  Instalada (MW)")
plt.title("Producción Energética Argentina según Fuente")

# Agrego  leyenda
plt.legend()
plt.show() #esto es necesario para visualizar

# Creamos el gráfico al estilo OO

# Creamos la figura y los axes
fig, ax = plt.subplots() # crear objetos

# Definimos series
ax.plot(x1, y1, label="Renovable") # Serie
ax.plot(x2, y2, label="Térmica") # Serie 2

# Modificamos labels y título
ax.set_xlabel("Período")
ax.set_ylabel("Potencia  Instalada (MW)")
ax.set_title("Producción Energética Argentina según Fuente (v2)")

# Agregamos leyenda
ax.legend()
fig.show()

# Graficar múltiples gráficos estilo pyplot

# ejemplo 2 ax en un fig
plt.figure(figsize=(14, 5))

# Definimos primer gráfico
plt.subplot(121) # subplot(nrows, ncols, index, **kwargs) donde nrows=1, ncols=2, index=1
plt.plot(x1, y1)
plt.title("Fuente Renovable")

# Definimos segundo gráfico
plt.subplot(122)
plt.plot(x2, y2)
plt.title("Fuente Térmica")

# Definimos título general de la figura
plt.suptitle("Ejemplo dos gráficos en una figura")
plt.show()

# Graficar múltiples gráficos estilo O-O

# ejemplo 2 ax en un fig
fig, ax = plt.subplots(figsize=(14, 5), ncols=2, nrows=1)

# Definimos primer gráfico
ax[0].plot(x1, y1)
ax[0].set_title("Fuente Renovable")

# Definimos segundo gráfico
ax[1].plot(x2, y2)
ax[1].set_title("Fuente Térmica")

# Definimos título general de la figura
fig.suptitle("Ejemplo dos gráficos en una figura")
fig.show()

"""### Otro ejemplo usando API de WB

Pueden ver la documentación [acá](https://wbdata.readthedocs.io/en/stable/)
"""

#!pip3 install -U wbdata
import wbdata
import pandas as pd

# Podemos ver todos los datos disponibles
wbdata.get_sources()

# Para este ejemplo vamos a usar source 14: indicadores de género
wbdata.get_indicators(source=14)

indicadores = {'HD.HCI.HLOS.FE':'scores_edu_fem','HD.HCI.HLOS.MA':'scores_edu_masc'}
#HD.HCI.HLOS.FE                   Harmonized Test Scores, Female
#HD.HCI.HLOS.MA                   Harmonized Test Scores, Male
data = wbdata.get_dataframe(indicadores, country=['USA','ARG'])

df = pd.DataFrame(data=data)

df.head()

df

ax = df.plot(kind='bar', title='Puntaje en educación')
ax.set_xlabel('País-Año',color='grey')
ax.set_ylabel('Puntaje',color='grey')
ax.legend(["Mujeres","Varones"])
# Acá estamos usando el index del df como xticklabels

"""Ahora buscamos hacer un gráfico solo con datos del año 2020"""

# Dejamos índice como columnas
df.reset_index(inplace=True)
df

print(df["date"].dtype) # no es numérica
df_2020 = df[df["date"]=="2020"]
df_2020

df_2020 = df_2020.set_index(["country", "date"])
df_2020

# Graficamos
ax = df_2020.plot(kind='bar', title='Puntaje en educación')
ax.set_xlabel('País-Año',color='grey')
ax.set_ylabel('Puntaje',color='grey')
ax.tick_params(axis="x", rotation=0)
ax.legend(["Mujeres","Varones"])


