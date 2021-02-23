import random

from world import World


class Ant:
    """
    Hormiga.
    """

    def __init__(self, world: World, initial=0, alpha=1, beta=1, learning=1):
        self.world = world
        self.initial = initial
        self.current_node = initial
        self.alpha = alpha
        self.beta = beta
        self.total_cost = 0
        self.learning = learning
        self.path = []
        self.visited = set()
        self.ignored = set()
        self.visited.add(initial)

    def find_destiny(self, destiny):
        """
        Ejecuta el algoritmo. destiny -> destino.
        """
        while self.current_node != destiny:
            available = self.get_available_paths()
            if not len(available):
                self.ignored.add(self.current_node)
                self.visited.remove(self.current_node)
                self.go_back()
                continue
            probabilities = self.get_node_probability(available)
            next_node = available[self.get_next_node(probabilities)]
            #print(next_node)
            self.move(next_node)
        # self.remove_cycles()
        #print(self.path)
        #print(self.total_cost)

    def go_back(self):
        """
        Regresa al último nodo.
        """
        last_step = self.path[len(self.path)-1]
        self.path.remove(last_step)
        self.total_cost -= float(self.world.graph[last_step[0]][last_step[1]])
        self.current_node = last_step[0]

    def move(self, next_node):
        """
        Mueve la hormiga al nodo next_node.
        """
        self.total_cost += float(self.world.graph[self.current_node][next_node])
        self.path.append((self.current_node, next_node))
        self.visited.add(next_node)
        self.current_node = next_node

    # def remove_cycles(self):
    #     def check_origin(list, value):
    #         for index, step in enumerate(list):
    #             if value[0] == step[0]:
    #                 list = list[0:index]
    #                 return True
    #         return False
    #     list = self.path.copy()
    #     list.reverse()
    #     reverse_path = []
    #     for step in list:
    #         if step[0] == self.initial:
    #             reverse_path.append(step)
    #             break
    #         elif check_origin(reverse_path, step):
    #             continue
    #         else:
    #             reverse_path.append(step)
    #     reverse_path.reverse() 
    #     self.path = reverse_path

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
        Devuelve una lista con las probabilidades de los nodos disponibles, available lista de nodos disponibles.
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
        Devuelve una lista de los indices de los nodos admisibles.
        """
        return [
            index
            for index, weight in enumerate(self.world.graph[self.current_node])
            if weight != 0 and index not in self.visited and index not in self.ignored
        ]

    def get_pheromone(self):
        """
        Devuelve la feromona actual de la hormiga.
        """
        return self.learning / self.total_cost
