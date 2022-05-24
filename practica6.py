import pandas as pd
import matplotlib.pyplot as plt

#crosstab
# Agregar el archivo para el análisis con pandas
df = pd.read_csv('datasets/users_modify.csv')
# Seleccionar las columnas a procesar
df = df[['gender', 'role']]
#Crear un cruce entre columnas y filas
ct = pd.crosstab(df['gender'], df['role']).plot(kind='bar')
plt.title("Gráfica para cruce de género y roles")

plt.xlabel("Género");
plt.ylabel("Cantidad de roles");

# for p in ct.patches:
#     ct.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')

plt.show()