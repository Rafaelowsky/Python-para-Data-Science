import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)

dataset = pd.read_csv('C:\\Users\\rzava\\OneDrive\\Documentos\\DataSciencePython\\Archivos\\db.csv', sep= ';')

# 1. Mostrar los primeros 10 registros

print(dataset.head(10))