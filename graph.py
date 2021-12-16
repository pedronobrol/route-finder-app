import geopy.distance
 
class Graph:
    def __init__(self, adjacent_list: dict, stations_dict: dict, lines: dict):
        self.adjacent_list = adjacent_list # Diccionario con distancia entre nodos adyacentes
        self.stations_dict = stations_dict # Diccionario con estaciones y sus cordenadas
        self.lines = lines 
        
 
    def get_neighbours(self, node: str) -> list:
        """ 
        Obtener nodos adyacentes del nodo pasado como parámetro
        """
        return self.adjacent_list[node]
    
    def reconstruct_path(self, node_couple: dict, min_f_node: str) -> list:
        """
        Recontruir camino secuencial a partir de una lista de adyacencias
        """
        path = []
        
        while node_couple[min_f_node] != min_f_node:
            path.append(min_f_node)
            min_f_node = node_couple[min_f_node]
        path.append(min_f_node)
        path.reverse()

        return path


    def get_best_node(self, open_list: list, g: list, destination: str) -> str:
        """ 
        Obtener nombre de nodo con f mínimo
        """
        min_f_node = open_list[0]

        for node in open_list:
            if g[node] + self.h(node, destination) < g[min_f_node] + self.h(min_f_node, destination):
                min_f_node = node
    
        return min_f_node
    
    def h(self, node: str, destination: str) -> float:
        """
        Estimar distancia según una herística consistente en calcular la distancia entre
        el nodo actual y el nodo destino y sumar un valor de transbordo si los nodos
        son de lineas distintas
        """
        transfer = True
        lines = ['green', 'red', 'blue']
        for line in lines:
            if node in self.lines[line] and destination in self.lines[line]:
                transfer = False

        current_node_coordinates = self.stations_dict[node]['coordinates']
        destination_coordinates = self.stations_dict[destination]['coordinates']
        result = geopy.distance.geodesic(current_node_coordinates, destination_coordinates).m 
        if transfer:
            result += 100   

        return result 

    def a_star_search(self, origin, destination) -> list:
        open_list = [origin]
        closed = []

        # Diccionario con las distancias entre origen y nodo (g)
        g = {} 
        g[origin] = 0

        # Diccionario con las parejas de nodos adyacentes
        node_couple = {}
        node_couple[origin] = origin

        while len(open_list) > 0:
            #Selecciona el nodo con f mínimo
            min_f_node = self.get_best_node(open_list, g, destination)

            # Si el nodo está en el destino. Hemos llegado
            if min_f_node == destination:
                reconstructed_path = self.reconstruct_path(node_couple, min_f_node) 
                print(f'Camino: {reconstructed_path}')
                return reconstructed_path
            
            # Verificar para todos los vecinos si ya están en la lista de visitados
            # (lista closed) o no visitados (lista open_list). Luego verificar cual 
            # el es el mejor camino y actualizar el coste. Si algún camino
            # visitado es mejor, pasarlo a por visistar. 
            for (name, distance) in self.get_neighbours(min_f_node):
                if name not in open_list and name not in closed:
                    open_list.append(name)
                    node_couple[name] = min_f_node
                    g[name] = g[min_f_node] + distance
                else:
                    if g[name] > g[min_f_node] + distance:
                        g[name] = g[min_f_node] + distance
                        node_couple[name] = min_f_node

                        if name in closed:
                            closed.remove(name)
                            open_list.append(name)
            open_list.remove(min_f_node)
            closed.append(min_f_node)

        print('El camino no existe')

        return None