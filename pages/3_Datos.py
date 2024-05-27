import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Asegúrate de que la configuración de la página se haga al principio
st.set_page_config(layout="wide")
# Set the page title and header
st.title("Simulador Costos")
# Ruta del archivo Excel directamente
file_path = 'datasets/costos.xlsx'  # Actualiza con la ruta correcta a tu archivo Excel

# Leer el archivo Excel
df = None
try:
    df = pd.read_excel(file_path, engine='openpyxl')
    st.write("Archivo Excel cargado exitosamente")
    st.dataframe(df)  # Muestra el DataFrame en la app de Streamlit
except Exception as e:
    st.error(f"Se produjo un error inesperado: {e}")

# Solo intenta acceder a las columnas si df está definido correctamente
if df is not None:
    # Limpiar los nombres de las columnas (opcional)
    df.columns = df.columns.str.strip()  # Eliminar espacios en blanco al inicio y al final de los nombres de las columnas
    try:
            cargoU = sorted(df['CARGO'].unique())
            areaU = sorted(df['AREA'].unique())
            servicioU = sorted(df['SERVICIO'].unique())
            costoU = sorted(df['COSTO'].unique())
            ventaU = sorted(df['VENTA'].unique())
            gananciaU = sorted(df['GANANCIA'].unique())
            margenU = sorted(df['MARGEN'].unique())

            # Mostrar los valores únicos en Streamlit (opcional)
            st.write("Valores únicos de CARGO:", cargoU)
            st.write("Valores únicos de AREA:", areaU)
            st.write("Valores únicos de SERVICIO:", servicioU)
    except Exception as e:
            st.error(f"Se produjo un error inesperado al procesar los datos: {e}")

# ___________________________________________________________

 # Calcular el MARGEN en porcentaje
    df['MARGEN'] = (df['GANANCIA'] / df['COSTO']) * 100

    # Agregar una tabla por CARGO
    st.subheader("Tabla por CARGO")
    cargo_table = df.groupby('CARGO').agg({'COSTO': 'sum', 'VENTA': 'sum', 'GANANCIA': 'sum', 'MARGEN': 'mean'}).sort_values(by='MARGEN', ascending=False)
    st.dataframe(cargo_table)

    # Agregar una tabla por AREA
    st.subheader("Tabla por AREA")
    area_table = df.groupby('AREA').agg({'COSTO': 'sum', 'VENTA': 'sum', 'GANANCIA': 'sum', 'MARGEN': 'mean'}).sort_values(by='MARGEN', ascending=False)
    st.dataframe(area_table)

    # Agregar una tabla por SERVICIO
    st.subheader("Tabla por SERVICIO")
    servicio_table = df.groupby('SERVICIO').agg({'COSTO': 'sum', 'VENTA': 'sum', 'GANANCIA': 'sum', 'MARGEN': 'mean'}).sort_values(by='MARGEN', ascending=False)
    st.dataframe(servicio_table)

    # Filtrar los datos por CARGO, AREA y SERVICIO
    selected_cargo = st.selectbox("Selecciona un CARGO:", df['CARGO'].unique())
    selected_area = st.selectbox("Selecciona un AREA:", df['AREA'].unique())
    selected_servicio = st.selectbox("Selecciona un SERVICIO:", df['SERVICIO'].unique())

    filtered_df = df[(df['CARGO'] == selected_cargo) & (df['AREA'] == selected_area) & (df['SERVICIO'] == selected_servicio)]

    # Graficar NOMBRE versus COSTO
    st.subheader("Gráfico de NOMBRE versus COSTO")
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df['NOMBRE'], y=filtered_df['COSTO'], name='COSTO'))
    fig.update_layout(title='COSTO por NOMBRE', xaxis_title='NOMBRE', yaxis_title='COSTO')
    st.plotly_chart(fig)