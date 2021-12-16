from graph import Graph
import pathlib
import os
import geopy.distance
import json
 
def read_data(filename='data.json') -> dict:
    """
    Leer data.json y obtener el objeto con datos
    """
    #Cargar datos del archivo json
    configFilePath = pathlib.Path(os.getcwd()) / filename
    with open(configFilePath, 'r') as configdata:
        data=configdata.read()

    return json.loads(data)

def get_neighbours(name: str, data: dict) -> list:
    """
    Obtener lista de pares nombre, distancia en metros de los adyacentes para
    una estación determianda
    """
    neighbours = []
    origin_coordinates = tuple(data[name]['coordinates'])
    for station in data[name]['adjacent_stations']: 
        destination_coordinates = tuple(data[station]['coordinates'])
        neighbour = (station, geopy.distance.geodesic(origin_coordinates, destination_coordinates).m)
        neighbours.append(neighbour)
    return neighbours

def get_adjacent_list() -> (dict, dict, dict):
    """
    Poner datos en el formato adecuado
    Devuelve:
    La lista de adyacencias con las distancias entre nodos: dict
    Las estaciones con sus coordenadas: dict
    Las lineas y sus estaciones: dict
    """
    adj_list = {}
    data = read_data()
    stations = data['subway_stations']
    lines = data['lines']
    for name, data in stations.items():
        adj_list[name] = get_neighbours(name, stations)
    return adj_list, stations, lines
    
def main() -> None:
    origin = input('Seleccione el origen: ')
    destination = input('Seleccione el destino: ')

    adjacent_list, stations, lines = get_adjacent_list()

    graph = Graph(adjacent_list, stations, lines)

    graph.a_star_search(origin, destination)
    
if __name__ == '__main__':
    main()
    
