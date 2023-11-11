# Este import es para poder usar las funciones de pandas y definirla como pd
import pandas as pd

# Estas dos lineas son para que solamente se muestren 10 filas y 10 columnas
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

# Guardamos el archivo en una variable
dataset = pd.read_csv('C:\\Users\\rzava\\OneDrive\\Documentos\\DataSciencePython\\Archivos\\db.csv', sep= ';')

# Mostrar los primeros 10 registros
print(dataset.head(10))

# Esta función muestra los tipos de datos de cada columna
print(dataset.dtypes)
