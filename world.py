import numpy as np


class World:
    def __init__(self):
        self.pheromones = np.zeros((8, 8))
        self.PATHS = np.zeros((8, 8))

        self.PATHS[1][2] = self.PATHS[2][1] = 5
        self.PATHS[1][3] = self.PATHS[3][1] = 3.1
        self.PATHS[1][6] = self.PATHS[6][1] = 5.2
        self.PATHS[2][3] = self.PATHS[3][2] = 4.9
        self.PATHS[2][7] = self.PATHS[7][2] = 5.2
        self.PATHS[3][5] = self.PATHS[5][3] = 3.7
        self.PATHS[3][6] = self.PATHS[6][3] = 3.2
        self.PATHS[3][7] = self.PATHS[7][3] = 3
        self.PATHS[5][4] = self.PATHS[4][5] = 5.5
        self.PATHS[5][6] = self.PATHS[6][5] = 4.7
        self.PATHS[7][4] = self.PATHS[4][7] = 4.8

        self.pheromones[1][2] = self.pheromones[2][1] = 0.1
        self.pheromones[1][3] = self.pheromones[3][1] = 0.1
        self.pheromones[1][6] = self.pheromones[6][1] = 0.1
        self.pheromones[2][3] = self.pheromones[3][2] = 0.1
        self.pheromones[2][7] = self.pheromones[7][2] = 0.1
        self.pheromones[3][5] = self.pheromones[5][3] = 0.1
        self.pheromones[3][6] = self.pheromones[6][3] = 0.1
        self.pheromones[3][7] = self.pheromones[7][3] = 0.1
        self.pheromones[5][4] = self.pheromones[4][5] = 0.1
        self.pheromones[5][6] = self.pheromones[6][5] = 0.1
        self.pheromones[7][4] = self.pheromones[4][7] = 0.1

    def update_pheromones(self, evaporation):
        self.pheromones = self.pheromones * (1-evaporation)
