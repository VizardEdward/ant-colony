import random

from world import World


class Ant:
    """
    Hormiga.
    """
    path = []

    def __init__(self, world: World, initial=0, alpha=1, beta=1, learning=1):
        self.world = world
        self.current_node = initial
        self.alpha = alpha
        self.alpha = alpha
        self.beta = beta
        self.total_cost = 0
        self.learning = learning

    def find_destiny(self, destiny):
        """
        Ejecuta el algoritmo. destiny -> destino
        """
        while self.current_node != destiny:
            available = self.get_available_paths()
            probabilities = self.get_node_probability(available)
            next_node = available[self.get_next_node(probabilities)]
            # print(next_node)
            self.move(next_node)
        # print(self.path)
        # print(self.total_cost)

    def move(self, next_node):
        """
        Mueve la hormiga al nodo next_node.
        """
        self.total_cost += float(self.world.graph[self.current_node][next_node])
        self.path.append((self.current_node, next_node))
        self.last_node = self.current_node
        self.current_node = next_node

    def get_next_node(self, probabilities):
        """
        Devuelve el índice del nodo al cual se debe mover la hormiga, 
        probabilities valores de las probabilidades asociadas a cada nodo.
        """
        start_value = 0
        random_number = random.random()
        next_node = None
        for index, last_value in enumerate(probabilities):
            next_node = index
            if random_number > start_value and random_number <= last_value + start_value:
                break
            start_value = last_value + start_value
        return next_node

    def get_node_probability(self, available):
        """
        Devuelve una lista con las probabilidades de los nodos disponibles, available lista de nodos disponibles
        """
        probabilities = [self.get_next_node_probability(n) for n in available]
        total = sum(probabilities)
        return [n / total for n in probabilities]

    def get_next_node_probability(self, next_node):
        """
        Devuelve la probabilidad del nodo next_node
        """
        return (self.world.pheromones[self.current_node][next_node] ** self.alpha
                ) / (self.world.graph[self.current_node][next_node] ** self.beta)

    def get_available_paths(self):
        """
        Devuelve una lista de los indices nodos a los 
        """
        return [
            index
            for index, weight in enumerate(self.world.graph[self.current_node])
            if weight != 0
        ]

    def get_pheromone(self):
        """
        Devuelve la feromona actual de la hormiga
        """
        return self.learning / self.total_cost
