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


def run(world, ants_number, iteration, origin, destiny, alpha=1, beta=1):
    for iter in range(iteration):
        ants_list = []
        for ant in range(ants_number):
            ant = Ant(world, origin, alpha, beta)
            ant.find_destiny(destiny)
            ants_list.append(ant)
        update_pheromones(world, ants_list)


# evaporation = 0.1
# world = World()
#
# def update_pheromones(ant):
#     my_pheromone = ant.get_pheromone()
#     for x,y in ant.path:
#         world.pheromones[x][y]= world.pheromones[x][y] + my_pheromone
#         world.pheromones[y][x]= world.pheromones[y][x] + my_pheromone

if __name__ == "__main__":
    world = read_world()
    run(world, 1, 1, 1, 4)
    # ant1 = Ant(world, 1, 4, 1, 1, 1)
    # ant1.find_destiny()
    # ant2 = Ant(world, 1, 4, 1, 1, 1)
    # ant2.find_destiny()
    # ant3 = Ant(world, 1, 4, 1, 1, 1)
    # ant3.find_destiny()
    # ant4 = Ant(world, 1, 4, 1, 1, 1)
    # ant4.find_destiny()
    # world.update_pheromones(evaporation)
    # update_pheromones(ant1)
    # update_pheromones(ant2)
    # update_pheromones(ant3)
    # update_pheromones(ant4)
    # print(ant4.total_cost)
