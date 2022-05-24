# Del archivo adult data
# Crear un análisis que permita conocer que género tiene más ingresos
# Cambiar el género a F o M
# Cambiar el income
#   Si es menor a 50 poner 49
#   Si es mayor poner 51
#   Crear un cruce de tabs o columnas

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/adult_data.csv')

# Cambiar el género a F o M
d = {'Male': 'M', 'Female': 'F'}
df['gender'] = df['gender'].apply(lambda x:d[x])

# Cambiar el income
#   Si es menor a 50 poner 49
#   Si es mayor poner 51
incomeData = {'<=50K': 49, '>50K': 51}
df['income'] = df['income'].apply(lambda x:incomeData[x])

# Crear un cruce de tabs o columnas
df = df[['gender', 'income']]

ct = pd.crosstab(df['gender'], df['income']).plot(kind='bar')
plt.title("Gráfica para conocer qué género gana más dinero")

plt.xlabel("Género");
plt.ylabel("Cantidad de personas")

for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')

plt.show()

df.to_csv('adult_data_modify.csv', index = False)