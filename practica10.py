import pandas as pd

# Leer el csv que usaremos, en este caso, 'banco.csv'
df = pd.read_csv('datasets/banco.csv')

# Dimensiones
print(df.shape)

# Datos faltantes
col_names = df.columns.tolist()
for column in col_names:
    print("Valores nulos en <" + column + ">: " + str(df[column].isnull().sum()))

# Valores nulos
print(df.isnull())

# Tipo de datos que tiene el dataset en General y por columna
# En general
print(df.dtypes)

# Por columna
for column in col_names:
    print("La columna <" + column + ">: Tiene el tipo de dato: " + column.dtypes())

# Uso de .info
print(df.info())

# Uso de .describe
print(df.describe())

# Datos duplicados en suma
print(df.duplicated().sum())