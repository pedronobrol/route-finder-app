# IA

Este programa encuentra la mejor ruta entre dos estaciones del metro de Kiev utilizando el algoritmo A*. 

La heurística que utiliza para averiguar f consiste en la distancia euclidiana entre el nodo actual y el destino, más
un coste de transbordo si el destino y el nodo actual se enceuntran en lineas distintas. 

Requisitos: python3

Pasos para ejecución: 

1- Crear entorno virtual:

python3 -m venv env

source env/bin/activate

2- Descargar dependencias

python3 install -r requirements.txt

3- Ejecutarlo 

Sin interfaz gráifica: python3 route_finder.py

Con interfaz gráfica: python3 gui.py
