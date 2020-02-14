"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time
import pandas as pd

class SineVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        if x > maximum or x < 0:
            return 0
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':

    pd.options.display.width = 0

    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    results = []
    for _ in range(50):
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.0)
        # print('Initial                      x: ' + str(p.initial)
        #       + '\t\tvalue: ' + str(p.value(initial))
        #       )

        # Solve the problem using hill-climbing.
        t_start = time.time()
        hill_solution = hill_climbing(p)
        t_hill = time.time() - t_start
        # print('Hill-climbing solution       x: ' + str(hill_solution)
        #       + '\tvalue: ' + str(p.value(hill_solution)) + '\ttime: ' + str(t_hill))

        # Solve the problem using simulated annealing.
        t_start = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        t_anneal = time.time() - t_start
        # print('Simulated annealing solution x: ' + str(annealing_solution)
        #       + '\tvalue: ' + str(p.value(annealing_solution)) + '\ttime: ' + str(t_anneal))

        results.append({"Initial": initial, "x_hill": hill_solution, "val_hill": p.value(hill_solution),
                        "time_hill": t_hill, "x_anneal": annealing_solution, "val_anneal": p.value(annealing_solution),
                        "time_anneal": t_anneal})

    results_df = pd.DataFrame.from_records(results)
    # filter out trials where simulated annealing got an invalid solution
    results_df = results_df[(0 <= results_df["x_anneal"]) & (results_df["x_anneal"] <= 30)]
    print(results_df.describe())
