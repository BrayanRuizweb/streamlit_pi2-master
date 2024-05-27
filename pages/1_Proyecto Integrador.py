import streamlit as st
import pandas as pd

st.header("Proyecto Integrador")

datos = {"Nombre": ["Ana", "Juan", "Pedro"],
         "Edad": [25, 30, 35],
         "Ciudad": ["Madrid", "Barcelona", "Sevilla"]}

# Convertir el diccionario a un DataFrame
df = pd.DataFrame(datos)

# st.table(df)



import streamlit as st
import pandas as pd

# Crear el DataFrame con la cantidad de animales por tipo
data = {
    'Tipo': ['Perro', 'Gato', 'Pájaro', 'Conejo', 'Hamster'],
    'Cantidad': [50, 30, 20, 10, 5]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
st.write(df)

# Graficar el DataFrame con un gráfico de barras
st.bar_chart(df.set_index('Tipo'))