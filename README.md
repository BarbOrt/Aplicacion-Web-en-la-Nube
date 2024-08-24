# Panel de Control de Aplicación Web en la Nube

El análisis que estamos llevando a cabo se centra en explorar y visualizar los datos de anuncios de venta de vehículos contenidos en el DataFrame `df`. Nuestro objetivo es obtener insights sobre diversos aspectos de estos anuncios. Para lograrlo, utilizamos una variedad de gráficos que nos ayudan a visualizar y comprender mejor los datos:

- **Histograma de Precios**: Observamos la distribución de los precios de los vehículos para entender la variabilidad en los precios y detectar posibles patrones o valores atípicos.
  
- **Gráfico de Dispersión de Precio vs. Año del Modelo**: Visualizamos la relación entre el precio y el año del modelo de los vehículos para identificar tendencias o patrones en la variación de precios a lo largo del tiempo.
  
- **Gráfico de Dispersión de Año del Modelo vs. Kilometraje**: Exploramos la relación entre la antigüedad del vehículo (representada por el año del modelo) y su kilometraje para entender cómo afecta la antigüedad del vehículo al kilometraje acumulado.
  
- **Gráfico de Barras de Distribución de Precios por Marca**: Comparamos los precios de los vehículos entre diferentes marcas para identificar qué marcas tienden a tener precios más altos o más bajos en general.
  
- **Gráfico de Barras de Proporción de Condiciones**: Utilizamos un gráfico de barras horizontales para visualizar la proporción de diferentes condiciones de los vehículos, facilitando la comparación entre las diferentes condiciones y proporcionando una representación más clara de la distribución.
  
- **Gráfico de Barras de Tendencia Temporal en la Cantidad de Días Listado**: Observamos la tendencia temporal en la cantidad de días que un vehículo está listado para la venta para identificar cambios o patrones en la duración de los anuncios a lo largo del tiempo.

En resumen, empleamos estos tipos específicos de gráficos para explorar diferentes aspectos de los datos de anuncios de venta de vehículos y obtener insights significativos que puedan informar en la toma de decisiones relacionadas con la compra o venta de vehículos.

## Enlace a la Aplicación Desplegada

Puedes visualizar la aplicación web desplegada en el siguiente enlace: [Aplicación en Render](https://proyecto-sprint-5-4b22.onrender.com/)

## Estructura del Proyecto

Este proyecto está estructurado de la siguiente manera:


. ├── README.md ├── app.py ├── vehicles_us.csv ├── requirements.txt └── notebooks └── EDA.ipynb └── .streamlit └── config.toml


- **README.md**: Este archivo que contiene la descripción del proyecto y las instrucciones.
- **app.py**: Archivo principal de la aplicación web construida con Streamlit.
- **vehicles_us.csv**: Conjunto de datos de anuncios de coches. Puedes reemplazarlo con otro dataset de tu elección.
- **requirements.txt**: Lista de dependencias del proyecto.
- **notebooks/EDA.ipynb**: Jupyter Notebook para el análisis exploratorio de datos.
- **.streamlit/config.toml**: Configuración para la aplicación Streamlit en Render.

## Instrucciones

### Paso 1: Configuración

1. **Crea un Repositorio en GitHub**: 
   - Crea un nuevo repositorio en GitHub con un archivo `README.md` y un archivo `.gitignore` (elige la plantilla de Python).

2. **Crea una Cuenta en Render**: 
   - Regístrate en [Render](https://render.com) y vincula tu cuenta de GitHub.

3. **Configura el Entorno Virtual**: 
   - Crea un entorno virtual en Python (por ejemplo, `vehicles_env`) e instala los siguientes paquetes:
     ```bash
     pip install pandas plotly-express streamlit
     ```
   - Guarda estas dependencias en el archivo `requirements.txt`:
     ```
     pandas
     plotly_express
     streamlit
     ```

4. **Instala VS Code**:
   - Clona tu repositorio de GitHub y ábrelo en VS Code.
   - Configura el intérprete de Python para que utilice el entorno virtual creado.

### Paso 2: Descarga del Archivo de Datos

- Descarga el conjunto de datos de anuncios de coches (`vehicles_us.csv`) o usa otro dataset de tu elección.
- Coloca el archivo CSV en el directorio del proyecto.

### Paso 3: Análisis Exploratorio de Datos

1. **Crea un Directorio para Notebooks**:
   - Crea un directorio llamado `notebooks` en el directorio de tu proyecto.
   
2. **Desarrolla un Jupyter Notebook**:
   - Crea un Jupyter Notebook llamado `EDA.ipynb` en el directorio `notebooks`.
   - Utiliza `plotly-express` para crear visualizaciones básicas como histogramas y gráficos de dispersión.

### Paso 4: Desarrollo del Cuadro de Mandos de la Aplicación Web

1. **Crea el Archivo Principal de la Aplicación**:
   - Crea un archivo `app.py` en la raíz del proyecto y añade el siguiente código básico:
     ```python
     import pandas as pd
     import plotly.express as px
     import streamlit as st

     # Leer los datos
     car_data = pd.read_csv('vehicles_us.csv')

     # Encabezado
     st.header('Panel de Control de Ventas de Coches')

     # Botón para construir un histograma
     hist_button = st.button('Construir histograma')
     if hist_button:
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         fig = px.histogram(car_data, x="odometer")
         st.plotly_chart(fig, use_container_width=True)

     # Botón para construir un gráfico de dispersión
     scatter_button = st.button('Construir gráfico de dispersión')
     if scatter_button:
         st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
         fig = px.scatter(car_data, x="odometer", y="price")
         st.plotly_chart(fig, use_container_width=True)
     ```

2. **Archivo de Configuración de Streamlit**:
   - Crea el archivo `.streamlit/config.toml` con el siguiente contenido:
     ```toml
     [server]
     headless = true
     port = 10000

     [browser]
     serverAddress = "0.0.0.0"
     serverPort = 10000
     ```

### Paso 5: Despliegue en Render

1. **Configura el Servicio en Render**:
   - Crea un nuevo servicio web en [Render](https://render.com) y enlázalo a tu repositorio de GitHub.
   - Configura el Build Command:
     ```bash
     pip install --upgrade pip && pip install -r requirements.txt
     ```
   - Configura el Start Command:
     ```bash
     streamlit run app.py
     ```

2. **Despliega y Verifica**:
   - Despliega la aplicación y verifica que esté accesible en la URL proporcionada por Render: `https://<APP_NAME>.onrender.com`.

### Cómo Enviar el Proyecto

- **Enlace al Repositorio de GitHub**: Asegúrate de que todos los archivos estén confirmados y empujados a tu repositorio de GitHub.
- **URL de la Aplicación en Render**: Añade la URL de tu aplicación desplegada en Render al `README.md`.

## Criterios de Evaluación

Los revisores evaluarán:
- La presencia de los archivos requeridos en el repositorio.
- La accesibilidad de la aplicación web a través de un navegador.
- La funcionalidad de la aplicación web, incluyendo:
  - Al menos un encabezado.
  - Al menos un histograma.
  - Al menos un gráfico de dispersión.
  - Al menos un botón o casilla de verificación.

¡Buena suerte con tu proyecto!
