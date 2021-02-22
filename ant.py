import random


class Ant:
    path = []

    def __init__(self, world, initial, destiny, alpha, beta, learning):
        self.world = world
        self.current_node = initial
        self.destiny = destiny
        self.alpha = alpha
        self.beta = beta
        self.total_cost = 0
        self.learning = learning

    def find_destiny(self):
        while self.current_node != self.destiny:
            available = self.get_available_paths()
            probabilities = self.get_node_probability(available)
            next_node = self.get_next_node(available,probabilities)
            print(next_node)
            self.move(next_node)
        self.remove_cycle()
        print(self.path)
        print(self.total_cost)

    def move(self, next_node):
        self.total_cost += self.world.PATHS[self.current_node][next_node]
        self.path.append((self.current_node, next_node))
        self.last_node = self.current_node
        self.current_node = next_node

    def get_next_node(self, available, probabilities):
        start_value = 0
        random_number = random.random()
        next_node = None
        for index, last_value in enumerate(probabilities):
            next_node = available[index]
            if random_number > start_value and random_number <= last_value + start_value:
                break
            start_value = last_value + start_value
        return next_node

    def get_node_probability(self, available):
        probabilities = [self.get_next_node_probability(n) for n in available]
        total = sum(probabilities)
        return [n / total for n in probabilities]

    def get_next_node_probability(self, next_node):
        return (self.world.pheromones[self.current_node][next_node]**self.alpha
                ) * (1 /
                     self.world.PATHS[self.current_node][next_node]**self.beta)

    def get_available_paths(self):
        return [
            index
            for index, weight in enumerate(self.world.PATHS[self.current_node])
            if weight != 0
        ]
    
    def get_pheromone(self):
        return self.learning/self.total_cost

    def remove_cycle(self):
        pass
    