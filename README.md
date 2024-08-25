# Panel de Control de Aplicación Web en la Nube

El objetivo de este proyecto es desarrollar y desplegar una aplicación web para la visualización de datos de anuncios de venta de vehículos. Utilizando `Streamlit` para la creación de la aplicación y `Plotly Express` para las visualizaciones, el proyecto incluye las siguientes funcionalidades:

- **Histograma de Precios**: Muestra la distribución de precios de los vehículos.
- **Gráfico de Dispersión de Precio vs. Año del Modelo**: Examina la relación entre el precio y el año del modelo de los vehículos.
- **Gráfico de Dispersión de Año del Modelo vs. Kilometraje**: Analiza la relación entre el año del modelo y el kilometraje de los vehículos.
- **Gráfico de Barras de Distribución de Precios por Marca**: Compara los precios de los vehículos entre diferentes marcas.
- **Gráfico de Barras de Proporción de Condiciones**: Muestra la distribución de las condiciones de los vehículos en diferentes categorías.
- **Gráfico de Barras de Tendencia Temporal en la Cantidad de Días Listado**: Observa cómo varía la cantidad de días que un vehículo permanece listado para la venta a lo largo del tiempo.

## Instrucciones para Completar el Proyecto

1. **Configuración**:
   - Crea un repositorio en GitHub con un archivo `README.md` y un archivo `.gitignore`.
   - Configura una cuenta en Render y vincúlala con tu repositorio de GitHub.
   - Crea un entorno virtual en Python e instala los paquetes necesarios (`pandas`, `plotly-express`, `streamlit`).

2. **Descarga del Archivo de Datos**:
   - Obtén el conjunto de datos `vehicles_us.csv` o utiliza otro dataset de tu elección y colócalo en el directorio del proyecto.

3. **Análisis Exploratorio de Datos**:
   - Desarrolla un Jupyter Notebook (`EDA.ipynb`) en el directorio `notebooks` para realizar el análisis exploratorio utilizando `plotly-express`.

4. **Desarrollo de la Aplicación Web**:
   - Crea un archivo `app.py` que contenga la lógica para la aplicación web en Streamlit.
   - Incluye gráficos interactivos y opciones para visualizar diferentes tipos de gráficos mediante botones o casillas de verificación.

5. **Despliegue en Render**:
   - Configura el despliegue en Render y asegúrate de que la aplicación sea accesible a través de la URL proporcionada por Render.

## Enlace a la Aplicación Desplegada

Puedes visualizar la aplicación web desplegada en el siguiente enlace: [Aplicación en Render](https://proyecto-sprint-5-4b22.onrender.com/)
