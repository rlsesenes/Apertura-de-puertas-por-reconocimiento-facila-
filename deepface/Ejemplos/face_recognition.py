#Importar biblioteca

from deepface import DeepFace
import pandas as pd

# buscar rostro
print ("buscando rostro")

#df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "/home/sesenes/Documents/GitHub/Apertura-de-puertas-por-reconocimiento-facila-/deepface/Faces/NICOLEKIDMAN.jpg", db_path = "/home/sesenes/Documents/GitHub/Apertura-de-puertas-por-reconocimiento-facila-/deepface/my_db", enforce_detection = "false")
print ("Resultado ")
print (df)
print ("Seleccion")
print (df.identity[0])
