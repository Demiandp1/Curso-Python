import tensorflow as ts
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#importando datos
temperature_df = pd.read_csv("celsius_a_fahrenheit.csv")

#Visualización
sns.scatterplot(temperature_df['Celsius'], temperature_df['Fahrenheit'])

#Cargando set de datos
x_train = temperature_df['Celsius']
y_train = temperature_df['Fahrenheit']

#Creando el modelo
