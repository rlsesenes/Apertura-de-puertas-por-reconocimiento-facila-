from deepface import DeepFace

print ("Se esta comparando dos imagenes para verificar identidad")
print ( "cargando...")

result = DeepFace.verify(img1_path = "/home/sesenes/Documents/GitHub/Apertura-de-puertas-por-reconocimiento-facila-/DeepFace/Faces/demi_1.jpeg", img2_path = "/home/sesenes/Documents/GitHub/Apertura-de-puertas-por-reconocimiento-facila-/DeepFace/Faces/Demi_2.jpeg")

print("estos son los resultados:")
print (result)
