import random

# Objective function
def fitness(x):
    return x ** 2

# Parameters
POPULATION_SIZE = 10
GENERATIONS = 20
MUTATION_RATE = 0.1
CHROMOSOME_LENGTH = 5

# Generate initial population
def create_population():
    return [
        random.randint(0, 31)
        for _ in range(POPULATION_SIZE)
    ]

# Selection
def selection(population):
    return max(population, key=fitness)

# Crossover
def crossover(parent1, parent2):
    p1 = format(parent1, '05b')
    p2 = format(parent2, '05b')

    point = random.randint(1, CHROMOSOME_LENGTH - 1)

    child = p1[:point] + p2[point:]
    return int(child, 2)

# Mutation
def mutation(chromosome):
    if random.random() < MUTATION_RATE:
        bit = random.randint(0, CHROMOSOME_LENGTH - 1)
        chromosome ^= (1 << bit)

    return chromosome

# Genetic Algorithm
def genetic_algorithm():
    population = create_population()

    for generation in range(GENERATIONS):
        new_population = []

        # Preserve the best solution
        best = max(population, key=fitness)
        new_population.append(best)

        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population)
            parent2 = selection(population)

            child = crossover(parent1, parent2)
            child = mutation(child)

            new_population.append(child)

        population = new_population

        best = max(population, key=fitness)
        print(
            f"Generation {generation + 1}: "
            f"x = {best}, Fitness = {fitness(best)}"
        )

    best_solution = max(population, key=fitness)

    print("\nBest Solution:", best_solution)
    print("Maximum Fitness:", fitness(best_solution))

# Run the algorithm
genetic_algorithm()