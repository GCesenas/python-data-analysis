import pandas as pd
import matplotlib.pyplot as plt

# Agregar el archivo para análisis con pandas
df = pd.read_csv('datasets/titanic.csv')
# Previsualizar
# print(df.head())

# Dimensión del dataframe
# print(df.shape)

# Contar
# print(df.count())

# Conocer la cantidad de datos faltantes
# col_names = df.columns.tolist()

# Iterar sobre la lista
# for column in col_names:
#     print("Valores nulos en <" + column + ">: " + str(df[column].isnull().sum()))

# Cambiar un diccionario con los valores originales por valores de reemplazo
d = {'male': 'M', 'female': 'F'}

# Utilizamos un lambda para el reemplazo en una sola línea
df['Sex'] = df['Sex'].apply(lambda x:d[x])

# Checar el cambio
# print(df['Sex'].head())

# Cruce de tabla o de información
ct = pd.crosstab(df['Survived'], df['Sex']).plot(kind = 'bar')
# plt.xlabel('Cantidad')
# plt.ylabel('Sobrevivientes')
# for barra in ct.containers:
#     ct.bar_label(barra, label_type = 'edge')

# plt.show()

pclass_survived = df.groupby(['Pclass', 'Sex'])['Survived'].sum()
# print(pclass_survived)

# Crear una figura de 15x15
plt.figure(figsize = (15, 15))
# Crear 2 columnas para renderizar varias gráficas
plt.subplot2grid((2, 3), (0, 0))
# Count de sobrevivientes y renderizarlo en tipo bar
t = df['Survived'].value_counts().plot(kind = 'bar')
plt.title('Sobrevivieron - Cuenta total')
plt.xlabel('Cantidad')
plt.ylabel('Sobrevivientes')

# Agregar valor a cada barra
for container in t.containers:
    t.bar_label(container, label_type = 'edge')

plt.show()

