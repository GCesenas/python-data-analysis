import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv('users_completo.csv')

#Selecciona solamente las columnas de género y el rol
df = df[['gender']]
#print(df.head())

#Contabilizar cuantos valores hay dentro de la columna "Género"
df['gender'].value_counts().plot(kind='pie')
plt.show()

#Tipos: barh, pie, bar, area, box, line, density, hexbin


