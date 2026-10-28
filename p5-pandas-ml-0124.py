import numpy as np
import pandas as pd
#Alan Romero NC 0124
## datos natriz 4 x 3
datos_alumnos=[
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2],
]
# poner nombre a las columnas
print("----Datos a partir de una matriz 4 x 3 ----")
# y almacenar la tabla en la variable df DataFrame
df=pd.DataFrame(datos_alumnos,columns=['ci','marcas','paquetes'])
print(df)
# datos a partir de un diccionario
print("----Datos a partir de un diccionario-----")
alumno_diccionario={
    "nombre":["Johan","Ricardo","Alan","Cristian","Scarlett","Ambar"],
    "califa":[100,90,70,90,80,60],
    "edad":[19,15,12,19,18,16]
}

estudiantes= pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Alan Romero NC 0124")
