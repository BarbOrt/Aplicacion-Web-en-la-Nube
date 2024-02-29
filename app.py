import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


df = pd.read_csv('vehicles_us.csv')

# Encabezado con texto
st.header("Análisis de Vehículos")

# Histograma de precios
show_price_histogram_button = st.button("Histograma de Precios")
if show_price_histogram_button:
    fig = px.histogram(df, x="price", title="Distribución de Precios de los Vehículos")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión de precio vs. año del modelo
show_scatter_checkbox = st.checkbox("Gráfico de Dispersión de Precio vs. Año del Modelo por modelo del auto")
if show_scatter_checkbox:
    fig = px.scatter(df, x="model_year", y="price", title="Variación del Precio según el Año del Modelo")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión de año del modelo vs. kilometraje
show_scatter_odometer_checkbox = st.checkbox("Gráfico de Dispersión de Año del Modelo vs. Kilometraje")
if show_scatter_odometer_checkbox:
    fig = px.scatter(df, x="model_year", y="odometer", title="Relación entre la Antigüedad del Vehículo y su Kilometraje")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de barras de distribución de precios por marca
show_bar_chart_button = st.button("Distribución de Precios según la Marca del Vehículo")
if show_bar_chart_button:
    fig = px.bar(df, x="model", y="price", title="Distribución de Precios según la Marca del Vehículo")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de barras de proporción de condiciones
show_condition_bar_button = st.button("Proporción de Condiciones de los Vehículos")
if show_condition_bar_button:
    condition_counts = df['condition'].value_counts()
    fig = px.bar(x=condition_counts.values, y=condition_counts.index, orientation='h', 
                 title="Proporción de Condiciones de los Vehículos", 
                 labels={'x': 'Cantidad', 'y': 'Condición'})
    st.plotly_chart(fig)

# Gráfico de barras de tendencia temporal en la cantidad de días listado
show_days_listed_bar_button = st.button("Tendencia Temporal en la Cantidad de Días Listado")
if show_days_listed_bar_button:
    df['date_posted'] = pd.to_datetime(df['date_posted'])  # Convertir a formato de fecha
    df['month_year'] = df['date_posted'].dt.to_period('M')  # Agrupar por mes y año
    days_listed_by_month = df.groupby('month_year')['days_listed'].mean().reset_index()
    fig = px.bar(days_listed_by_month, x='month_year', y='days_listed', 
                 title="Tendencia Temporal en la Cantidad de Días Listado", 
                 labels={'month_year': 'Mes y Año', 'days_listed': 'Días Listado Promedio'})
    st.plotly_chart(fig)
