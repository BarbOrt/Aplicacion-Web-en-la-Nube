# Panel de Control de Aplicación Web en la Nube

Este repositorio contiene una aplicación web desarrollada para la visualización de datos de anuncios de venta de vehículos. Utilizando `Streamlit` para la creación de la aplicación y `Plotly Express` para las visualizaciones, la aplicación proporciona las siguientes funcionalidades:

- **Histograma de Precios**: Muestra la distribución de precios de los vehículos.
- **Gráfico de Dispersión de Precio vs. Año del Modelo**: Examina la relación entre el precio y el año del modelo de los vehículos.
- **Gráfico de Dispersión de Año del Modelo vs. Kilometraje**: Analiza la relación entre el año del modelo y el kilometraje de los vehículos.
- **Gráfico de Barras de Distribución de Precios por Marca**: Compara los precios de los vehículos entre diferentes marcas.
- **Gráfico de Barras de Proporción de Condiciones**: Muestra la distribución de las condiciones de los vehículos en diferentes categorías.
- **Gráfico de Barras de Tendencia Temporal en la Cantidad de Días Listado**: Observa cómo varía la cantidad de días que un vehículo permanece listado para la venta a lo largo del tiempo.

## Estructura del Repositorio

- **`app.py`**: Archivo principal de la aplicación web en Streamlit.
- **`vehicles_us.csv`**: Conjunto de datos utilizado para la visualización.
- **`requirements.txt`**: Archivo de requisitos que incluye las dependencias del proyecto (`pandas`, `plotly-express`, `streamlit`).
- **`notebooks/EDA.ipynb`**: Jupyter Notebook para el análisis exploratorio de datos.
- **`.streamlit/config.toml`**: Archivo de configuración de Streamlit para el despliegue en Render.

## Enlace a la Aplicación Desplegada

Haz clic en el siguiente icono para visualizar la aplicación web desplegada:

[![Ver Aplicación](https://img.shields.io/badge/Ver%20Aplicación%20-Web%20App-blue)](https://proyecto-sprint-5-4b22.onrender.com/)
