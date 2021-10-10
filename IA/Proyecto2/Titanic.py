#importando librerias a utilizar
import pandas as pd
import numpy as np

#importando datos a utilizar
url_test = "https://www.kaggle.com/c/titanic/data?select=test.csv"
url_train = "https://www.kaggle.com/c/titanic/data?select=train.csv"

#guardando datos en variables
df_test = pd.read_csv(url_test)
df_train = pd.read_csv(url_train)

#guardando datos a utilizar para que esten siempre disponibles en la pc
dir_test = "E:\\Users\elmon\Desktop\Curso Python\IA\Proyecto2\titanic_test.csv"
dir_train = "E:\\Users\elmon\Desktop\Curso Python\IA\Proyecto2\titanic_train.csv"

df_test.to_csv(dir_test)
df_train.to_csv(dir_train)
