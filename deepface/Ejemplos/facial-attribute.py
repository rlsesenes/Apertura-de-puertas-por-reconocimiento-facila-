from deepface import DeepFace


obj = DeepFace.analyze(img_path = "/home/sesenes/Documents/GitHub/Apertura-de-puertas-por-reconocimiento-facila-/DeepFace/Faces/image.jpeg", actions = ['age', 'gender', 'race', 'emotion'])

print ("El resultado del analisi es: ")
print (obj)