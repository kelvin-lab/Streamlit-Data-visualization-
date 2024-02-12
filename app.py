import streamlit as st
import pandas as pd 
import plotly.express as px


@st.cache_data
def load_data(file_path):
    """
    The function `load_data` reads a CSV file and returns a DataFrame, or displays an error message if
    the file is not found.
    
    :param file_path: The file path is the location of the CSV file that you want to load. It should be
    a string that specifies the path to the file, including the file name and extension. For example,
    "C:/Users/username/data.csv" or "data/data.csv"
    :return: a pandas DataFrame object.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError as e:
        st.error(f"Error al cargar el archivo CSV: {e}")

# Application Title
st.title('Explorador de Datos de Vehículos')

# Application description
st.write('Bienvenido al Explorador de Datos de Vehículos. Utiliza las opciones a continuación para explorar los datos disponibles.')

# Load the CSV file
file_path = 'vehicles_us.csv'
df_vehicles = load_data(file_path)

# Allow users to select columns
default_columns = ['price', 'model_year', 'model', 'condition', 'date_posted']
columns_to_show = st.multiselect('Selecciona las columnas:', df_vehicles.columns.tolist(), default=default_columns)
st.subheader('Visualizar DataFrame')
st.dataframe(df_vehicles[columns_to_show])

# Options to display data
option = st.selectbox(
    'Lista de gráficas:',
    ('Histograma', 'Gráfico de dispersión'), index=None, placeholder="Seleccione un gráfico..."
)

# Display of selected data
if option == 'Histograma':
    st.subheader('Histograma de Odómetro')
    column_for_histogram = st.selectbox('Selecciona una columna para el histograma:', df_vehicles.columns.tolist(), index=0)
    fig = px.histogram(df_vehicles, x=column_for_histogram)
    st.plotly_chart(fig, use_container_width=True)
elif option == 'Gráfico de dispersión':
    st.subheader('Gráfico de dispersión de Precio vs Odómetro')
    fig = px.scatter(df_vehicles, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)  
