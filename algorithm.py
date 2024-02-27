from fitness import *
import random
from copy import deepcopy
import pylab


POPULATION_SIZE = 1500
P_CROSSOVER = 0.9
P_MUTATION = 0.8
MAX_GENERATIONS = 300

random.seed(21)


def create_individual():
    weights = []
    for i in range(number_of_points):
        weights.append(random.randint(0, number_of_points - 1))
    return weights


population = []
for i in range(POPULATION_SIZE):
    population.append(create_individual())

max_fit = []
avg_fit = []
min_fit = []

generations_count = 0

while generations_count < MAX_GENERATIONS:
    offsprings = []
    population = sorted(population, key=lambda x: - fitness(x))
    elite = 4
    for i in range(elite):
        offsprings.append(deepcopy(population[i]))

    for i in range(elite, POPULATION_SIZE):
        i1 = i2 = i3 = 0
        while i1 == i2 or i2 == i3 or i3 == i1:
            i1 = random.randint(elite, POPULATION_SIZE - 1)
            i2 = random.randint(elite, POPULATION_SIZE - 1)
            i3 = random.randint(elite, POPULATION_SIZE - 1)
        offsprings.append(deepcopy(max(population[i1], population[i2], population[i3], key=lambda x: fitness(x))))

    for i in range(elite, POPULATION_SIZE // 2 + elite // 2):
        if random.random() < P_CROSSOVER:
            parent1 = offsprings[i]
            parent2 = offsprings[i + POPULATION_SIZE // 2 - elite // 2]
            for gene in range(len(parent1)):
                if random.random() < 0.05:
                    parent1[gene], parent2[gene] = parent2[gene], parent1[gene]

    for i in range(elite, POPULATION_SIZE):
        if random.random() < P_MUTATION:
            for gene in range(len(offsprings[i])):
                if random.random() < 0.05:
                    offsprings[i][gene] = random.randint(0, number_of_points - 1)

    fitness_values = []
    for offspring in offsprings:
        fitness_values.append(fitness(offspring))
    max_fit.append(max(fitness_values))
    min_fit.append(min(fitness_values))
    avg_fit.append(sum(fitness_values) / len(fitness_values))
    population = offsprings
    generations_count += 1

population = sorted(population, key=lambda x: - fitness(x))
best_solution = population[0]

pylab.subplots(figsize=(16, 7))
pylab.subplot(1, 2, 1)
x = []
y = []
for i in range(-1, len(best_solution)):
    x.append(points[best_solution[i]][0])
    y.append(points[best_solution[i]][1])
    if i != -1:
        pylab.scatter(x[i], y[i], color='black', s=15)
pylab.plot(x, y)
pylab.title('The shortest received path')

pylab.subplot(1, 2, 2)
pylab.plot(max_fit, color='green', label='best individual')
pylab.plot(min_fit, color='red', label='worst individual')
pylab.plot(avg_fit, color='blue', label='average individual')
pylab.legend()
pylab.title('Learning dynamics')

pylab.show()
