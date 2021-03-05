import os
from pathlib import Path

from dotenv import load_dotenv

from ant import Ant
from world import World
import matplotlib.pyplot as plt


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


def update_pheromones(world, ants):
    world.evaporate()
    ant_minim = ants[0]
    for ant in ants:
        # if ant_minim.total_cost > ant.total_cost:
        #     ant_minim = ant
        world.update_pheromones(ant.path, ant.get_pheromone())
    # world.update_pheromones(ant_minim.path, ant_minim.get_pheromone())


def plot(y):
    plt.plot(range(1, len(y) + 1), y)
    plt.xlabel("Iteración")
    plt.ylabel("Costo mínimo")
    plt.show()


def run(world, ants_number, iterations, origin, destiny, learning=1, alpha=1, beta=1):
    min_list = []
    for _ in range(iterations):
        ants_list = []
        cost_list = []
        for _ in range(ants_number):
            ant = Ant(world, origin - 1, alpha, beta, learning)
            ant.find_destiny(destiny - 1)
            ants_list.append(ant)
            cost_list.append(ant.total_cost)
        min_cost = min(cost_list)
        min_list.append(min_cost)
        update_pheromones(world, ants_list)
    plot(min_list   )


if __name__ == "__main__":
    if os.environ.get("SKIP_DOTENV", "") != "1":
        load_dotenv(dotenv_path=Path('.') / '.env')
    world = read_world()
    ANT_NUMBERS = int(os.environ.get("ANT_NUMBERS", 3))
    ITERATIONS_NUMBER = int(os.environ.get("ITERATIONS_NUMBER", 1000))
    ORIGIN = int(os.environ.get("ORIGIN", 1))
    DESTINY = int(os.environ.get("DESTINY", 4))
    LEARNING = float(os.environ.get("LEARNING", 1))
    run(world, ants_number=ANT_NUMBERS, iterations=ITERATIONS_NUMBER, origin=ORIGIN, destiny=DESTINY, learning=LEARNING)
