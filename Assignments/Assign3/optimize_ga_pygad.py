import main as objective_function
import pandas as pd
import numpy as numpy
import pygad as pygad


#imported_df = pd.read_csv("./file_import_and_graph/DOE_tanner.csv", index_col=0)
npv_array = []
#mtot_array = []
#capex_array = []
experiment_tuple = (5,2,12,28000,700,1800,3200,4800,5500,7000)

def fitness_func(ga_instance, solution, solution_idx):
    # The fitness function calulates the sum of products between each input and its corresponding weight.
    #output = objective_function.experiment(experiment_tuple)
    output = numpy.sum(solution*experiment_tuple)
    # The value 0.000001 is used to avoid the Inf value when the denominator numpy.abs(output - desired_output) is 0.0.
    fitness = 1/((output)+0.0000001)
    return fitness

# Bounds and constraints (see scipy.optimize.differential_evolution documentation)
gene_space = [[5,10,20],
              [1,2,3],
              [4,12,20],
              {'low':1000,'high':55000},
              {'low':500,'high':700},
              {'low':900,'high':1800},
              {'low':2300,'high':3200},
              {'low':3800,'high':4800},
              {'low':5000,'high':6000},
              {'low':6000,'high':7000}]

#gene_space = [[5,10,20],
#              [1,2,3],
#              [4,12,20],
#              [1000,28000,55000],
#              [500,600,700],
#              [900,1300,1800],
#              [2300,2800,3200],
#              [3800,4400,4800],
#              [5000,5500,6000],
#              [6000,6500,7000]]

ga_instance = pygad.GA(num_generations=1500,
                       num_parents_mating=50,
                       fitness_func=fitness_func,
                       sol_per_pop=100,
                       #initial_population=experiment_tuple,
                       parent_selection_type="rws",
                       num_genes=len(experiment_tuple),
                       mutation_percent_genes=40,
                       gene_space=gene_space)


#NPV = objective_function.experiment(experiment_tuple)



ga_instance.run()
ga_instance.plot_fitness(title="PyGAD with Adaptive Mutation", linewidth=5)

print(ga_instance)

solution, solution_fitness, solution_idx = ga_instance.best_solution()
NPV_final = objective_function.experiment(solution)
print("final NPV: {NPV_final}".format(NPV_final=NPV_final))
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))
