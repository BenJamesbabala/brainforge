import numpy as np
from matplotlib import pyplot as plt

from brainforge.evolution import Population


def upscale(ind):
    x = np.array(ind) - 0.5
    x *= 10.
    return x


def fitness(ind):
    x = upscale(ind)
    return np.sum(x**2),


def matefn(ind1, ind2):
    return (ind1 + ind2) / 2.

pop = Population(
    loci=2,
    fitness_function=fitness,
    fitness_weights=[1.],
    mate_function=matefn,
    limit=100)

pop.individuals += 0.5
pop.individuals = np.clip(pop.individuals, 0., 1.)

X, Y = pop.individuals.T
plt.ion()
obj = plt.scatter(X, Y, color="red", vmin=-5., vmax=5.)
plt.show()
for i in range(100):
    pop.run(1, verbosity=0)
    plt.cla()
    plt.scatter(*pop.individuals.T, color="red", vmin=-5., vmax=5.)
    plt.pause(0.1)
