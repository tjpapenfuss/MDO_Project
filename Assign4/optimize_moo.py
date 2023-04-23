import main_moo as objective_function
import pandas as pd
from scipy.optimize import minimize
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import numpy as np
from pymoo.core.problem import Problem
import numpy as np
from pymoo.core.problem import ElementwiseProblem
from pymoo.termination import get_termination
from pymoo.optimize import minimize
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import FloatRandomSampling

# Import DOE for the initial guess. 
imported_df = pd.read_csv("./file_import_and_graph/DOE_tanner.csv", index_col=0)


# Bounds and constraints (see scipy.optimize.minimize documentation)
# The following variables are used in the objective function:
# number of wells, bounds = (5,20)
bound_num_wells = (5,20)
# num point connections, bounds = (1, 3)
bound_num_connections = (1,3)
# pipeline diameter, bounds = (4, 20)
bound_pipeline_diameter = (4,20)
# pipeline length, bounds = (1000, 55000)
bound_pipeline_length = (1000,55000)
# pressure into the facility, bounds = (500, 700)
bound_p2 = (500,700)
# pressure 4, bounds = (900, 1800)
bound_p4 = (900,1800)
# pressure 6, bounds = (2300, 3200)
bound_p6 = (2300,3200)
# pressure 8, bounds = (3800, 4800)
bound_p8 = (3800,4800)
# pressure 10, bounds = (5000, 6000)
bound_p10 = (5000,6000)
# pressure 12, bounds = (6000, 7000)
bound_p12 = (6000,7000)

# constraints
# 10,000 <= Qinj <= 100,000
# PWH > 0
# PWF > Pres
# Qinj * num_wells * time <= Qmax

# Setup bounds from above. 
bnds = (bound_num_wells, bound_num_connections, 
        bound_pipeline_diameter, bound_pipeline_length, bound_p2, 
        bound_p4, bound_p6, bound_p8, bound_p10, bound_p12)

# Create the initial guess from the DOE. 
for n in range(0, 4):
    experiment_tuple = (imported_df.loc[n]["Number of Wells"],
                            imported_df.loc[n]["Number of Connections"],
                            imported_df.loc[n]["Pipeline Diameter"],
                            imported_df.loc[n]["Pipeline Length"],
                            imported_df.loc[n]["p2"],
                            imported_df.loc[n]["p4"],
                            imported_df.loc[n]["p6"],
                            imported_df.loc[n]["p8"],
                            imported_df.loc[n]["p10"],
                            imported_df.loc[n]["p12"])
    print(experiment_tuple)

    # Minimize objective function.
    # result = minimize(objective_function.experiment, experiment_tuple, method='SLSQP', bounds=bnds)
    # print(result)

    # class SphereWithConstraint(Problem):

    #     def __init__(self):
    #         super().__init__(n_var=10, n_obj=1, n_ieq_constr=1, xl=0.0, xu=1.0)

    #     def _evaluate(self, x, out, *args, **kwargs):
    #         out["F"] = np.sum((x - 0.5) ** 2, axis=1)
    #         out["G"] = 0.1 - out["F"]
            
            
    # # problem = get_problem("zdt1")

    # class ElementwiseSphereWithConstraint(ElementwiseProblem):

    #     def __init__(self):
    #         xl = np.zeros(10)
    #         xl[0] = -5.0

    #         xu = np.ones(10)
    #         xu[0] = 5.0

    #         super().__init__(n_var=10, n_obj=1, n_ieq_constr=2, xl=xl, xu=xu)

    #     def _evaluate(self, x, out, *args, **kwargs):
    #         out["F"] = np.sum((x - 0.5) ** 2)
    #         out["G"] = np.column_stack([0.1 - out["F"], out["F"] - 0.5])


    # algorithm = NSGA2(pop_size=100)

    # res = minimize(problem,
    #                algorithm,
    #                ('n_gen', 200),
    #                seed=1,
    #                verbose=True)

    # plot = Scatter()
    # plot.add(problem.pareto_front(), plot_type="line", color="black", alpha=0.7)
    # plot.add(res.F, color="red")
    # plot.show()



    class MyProblem(ElementwiseProblem):

        def __init__(self):
            super().__init__(n_var=10,
                            n_obj=2,
                            n_ieq_constr=0,
                            xl=np.array([5,1,4,1000,500,900,2300,3800,5000,6000]),
                            xu=np.array([20,3,20,55000,700,1800,3200,4800,6000,7000]))

        def _evaluate(self, x, out, *args, **kwargs):
            NPV, CAPEX_Total = objective_function.experiment(x)    
            f1 = NPV
            f2 = CAPEX_Total



    # $$$$$$$$$$
    # bound_num_wells = (5,20)
    # # num point connections, bounds = (1, 3)
    # bound_num_connections = (1,3)
    # # pipeline diameter, bounds = (4, 20)
    # bound_pipeline_diameter = (4,20)
    # # pipeline length, bounds = (1000, 55000)
    # bound_pipeline_length = (1000,55000)
    # # pressure into the facility, bounds = (500, 700)
    # bound_p2 = (500,700)
    # # pressure 4, bounds = (900, 1800)
    # bound_p4 = (900,1800)
    # # pressure 6, bounds = (2300, 3200)
    # bound_p6 = (2300,3200)
    # # pressure 8, bounds = (3800, 4800)
    # bound_p8 = (3800,4800)
    # # pressure 10, bounds = (5000, 6000)
    # bound_p10 = (5000,6000)
    # # pressure 12, bounds = (6000, 7000)
    # bound_p12 = (6000,7000)

    # $$$$$$$$
            # g1 = 2*(x[0]-0.1) * (x[0]-0.9) / 0.18
            # g2 = - 20*(x[0]-0.4) * (x[0]-0.6) / 4.8

            out["F"] = [f1, f2]
            # out["G"] = [g1, g2]

    # _evaluate(main)

    problem = MyProblem()


    algorithm = NSGA2(
        pop_size=70,
        n_offsprings=10,
        sampling=FloatRandomSampling(),
        crossover=SBX(prob=0.9, eta=15),
        mutation=PM(eta=20),
        eliminate_duplicates=True
    )

    termination = get_termination("n_gen", 40)


    res = minimize(problem,
                algorithm,
                termination,
                seed=1,
                save_history=True,
                verbose=True)

    X = res.X
    F = res.F

    print(X)
    print(F)

    import matplotlib.pyplot as plt
    xl, xu = problem.bounds()
    # plt.figure(figsize=(7, 5))
    # plt.scatter(X[:, 0], X[:, 1], s=30, facecolors='none', edgecolors='r')
    # plt.xlim(xl[0], xu[0])
    # plt.ylim(xl[1], xu[1])
    # plt.title("Design Space")
    # plt.show()
    # plt.figure(figsize=(7, 5))
    # plt.scatter(F[:, 0], F[:, 1], s=30, facecolors='none', edgecolors='blue')
    # plt.title("Objective Space")
    # plt.show()