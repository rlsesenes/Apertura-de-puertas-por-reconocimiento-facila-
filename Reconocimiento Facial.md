# Introducción Python- Reconocimiento Facial 
3.1 Generar una base de datos de rostros 
4. Crear una carpeta llamada my_db
5. Crear una carpeta por persona 
6. Agregar al menos 5 imagenes que describan dicho rostro 
7. Hacerlo para al menos 3 personas
8. Formato JPG o PNG
9. Maximo 800 x 800 pix
10. Minimo 120x120 pix
11. Fondo diferenciable 


# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "/home/sesenes/Documents/GitHub/Apertura-de-puertas-por-reconocimiento-facila-/DeepFace/Faces/NICOLEKIDMAN.jpg", db_path = "/home/sesenes/Documents/GitHub/Apertura-de-puertas-por-reconocimiento-facila-/DeepFace/my_db", enforce_detection = "false")
print ("Resultado ")
print (df)
print ("Seleccion")
print (df.identity[0])