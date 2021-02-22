from ant import Ant
from world import World

evaporation = 0.1
world = World()

def update_pheromones(ant):
    my_pheromone = ant.get_pheromone()
    for x,y in ant.path:
        world.pheromones[x][y]= world.pheromones[x][y] + my_pheromone
        world.pheromones[y][x]= world.pheromones[y][x] + my_pheromone

if __name__ == "__main__":
    ant1 = Ant(world, 1, 4, 1, 1, 1)
    ant1.find_destiny()
    ant2 = Ant(world, 1, 4, 1, 1, 1)
    ant2.find_destiny()
    ant3 = Ant(world, 1, 4, 1, 1, 1)
    ant3.find_destiny()
    ant4 = Ant(world, 1, 4, 1, 1, 1)
    ant4.find_destiny()
    world.update_pheromones(evaporation)
    update_pheromones(ant1)
    update_pheromones(ant2)
    update_pheromones(ant3)
    update_pheromones(ant4)
    print(ant4.total_cost)

