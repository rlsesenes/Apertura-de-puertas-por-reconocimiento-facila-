# MQTT-PYTHON

1. intstalar la libreria Paho.MQTT siguiendo el procedimiento mostrado en: 

https://pypi.org/project/paho-mqtt/

2. Crear una carpeta llamada MQTT en el repositorio Apertura de puertas por reconomiento facial
3. Crear un programa en python que publique en MQTT. Crear el archivo .py mqtt-python.py donde se registrara el código 



https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

Buscar el Broker con: `nslookup broker.hivemq.com `

Broker : 3.120.0.43
Tema codioIoT/mqtt/python
mensaje: Hola Python-MQTT: Roy López

mosquitto_sub -h 3.120.0.43 -t codioIoT/mqtt/python

mosquitto_pub -h 3.120.0.43 -t codioIoT/mqtt/python-m "Hola Mosquitto-MQTT: Roy Lopez"


Crear un nuevo programa en python que envie por MQTT el análisis facial 
1. Crear una nueva carpeta en el repositorio Apertura de puertas denominada como python-apertura donde se guardará el programa para enviar la información 
2. Genear el nuevo programa que envíe la información. 


