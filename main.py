from ant import Ant
from world import World


def read_world():
    file = open("path.in", "rt")
    nodes_number, globally_pheromones, evaporation = tuple(file.readline().strip().split(" "))
    world = World(int(nodes_number), float(globally_pheromones), float(evaporation))
    for line in file.readlines():
        elements = line.strip().split(" ")
        node_1 = int(elements[0])
        node_2 = int(elements[1])
        weight = float(elements[2])
        pheromones = None
        if len(elements) > 3:
            pheromones = elements[3]
        world.set_graph_info(node_1 - 1, node_2 - 1, weight, pheromones)
    return world


def update_pheromones(world, ants: list):
    world.evaporate()
    for ant in ants:
        world.update_pheromones(ant.path, ant.get_pheromone())


def run(world, ants_number, iterations, origin, destiny, alpha=1, beta=1):
    for iter in range(iterations):
        ants_list = []
        for ant in range(ants_number):
            ant = Ant(world, origin, alpha, beta)
            ant.find_destiny(destiny)
            ants_list.append(ant)
        update_pheromones(world, ants_list)


if __name__ == "__main__":
    world = read_world()
    run(world, ants_number=1, iterations=1, origin=1, destiny=4)
