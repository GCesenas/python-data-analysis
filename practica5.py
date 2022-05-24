import matplotlib.pyplot as plt
import pandas as pd

#Agregar csv al dataframe
df = pd.read_csv('users_completo.csv')

#Seleccionar las columnas a analizar
df = df[["car","department"]]


#Groupby (Agrupar las columnas)
group=df.groupby(["car","department"])
#print(group)

print(group.size().reset_index(name='counts'))