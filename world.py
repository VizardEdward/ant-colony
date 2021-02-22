import numpy as np


class World:
    def __init__(self, nodes_number, globally_pheromones=None, evaporation=0.1):
        self.pheromones = np.zeros((nodes_number, nodes_number))
        self.graph = np.zeros((nodes_number, nodes_number))
        self.globally_pheromones = globally_pheromones
        self.evaporation = evaporation

    def evaporate(self):
        self.pheromones = self.pheromones * (1 - self.evaporation)

    def update_pheromones(self, path, pheromones):
        for x, y in path:
            self.pheromones[x][y] = self.pheromones[x][y] + pheromones
            self.pheromones[y][x] = self.pheromones[y][x] + pheromones

    def set_graph_info(self, node_1, node_2, weight, pheromones=None):
        self.graph[node_1][node_2] = weight
        self.graph[node_2][node_1] = weight
        self.set_pheromones(node_1, node_2, pheromones)

    def set_pheromones(self, node_1, node_2, pheromones=None):
        if not pheromones:
            self.pheromones[node_1][node_2] = self.globally_pheromones
            self.pheromones[node_2][node_1] = self.globally_pheromones
        else:
            self.pheromones[node_1][node_2] = pheromones
            self.pheromones[node_2][node_1] = pheromones
