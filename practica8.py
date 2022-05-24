import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/movie_metadata.csv')

df = df[['color', 'content_rating']]

ct = pd.crosstab(df['color'], df['content_rating']).plot(kind='bar')
plt.title("Gráfica")

plt.xlabel("A color o blanco y negro");
plt.ylabel("Cantidad de películas con cada rating")

for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')


plt.show()