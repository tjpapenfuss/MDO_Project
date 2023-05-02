import main as objective_function
import pandas as pd
from scipy.optimize import minimize
from pyswarm import pso


# Import DOE for the initial guess. 
imported_df = pd.read_csv("./file_import_and_graph/DOE_tanner.csv", index_col=0)
NPV = []
for index, row in imported_df.iterrows():
    # print(index, row)
    experiment_tuple = (imported_df.loc[index]["Number of Wells"],
                        imported_df.loc[index]["Number of Connections"],
                        imported_df.loc[index]["Pipeline Diameter"],
                        imported_df.loc[index]["Pipeline Length"],
                        imported_df.loc[index]["p2"],
                        imported_df.loc[index]["p4"],
                        imported_df.loc[index]["p6"],
                        imported_df.loc[index]["p8"],
                        imported_df.loc[index]["p10"],
                        imported_df.loc[index]["p12"])
    NPV.append(objective_function.experiment(experiment_tuple))

# print("The NPV values are:")
# print(NPV)
frames = [imported_df, pd.DataFrame(NPV, columns=["NPV"])]
result = pd.concat(frames, axis=1)
result.to_csv("DOE_NPV.csv")

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
lb = [bound_num_wells[0], bound_num_connections[0], 
        bound_pipeline_diameter[0], bound_pipeline_length[0], bound_p2[0],
        bound_p4[0], bound_p6[0], bound_p8[0], bound_p10[0], bound_p12[0]]
ub = [bound_num_wells[1], bound_num_connections[1], 
        bound_pipeline_diameter[1], bound_pipeline_length[1], bound_p2[1],
        bound_p4[1], bound_p6[1], bound_p8[1], bound_p10[1], bound_p12[1]]

# Create the initial guess from the DOE. 
experiment_tuple = (imported_df.loc[19]["Number of Wells"],
                        imported_df.loc[19]["Number of Connections"],
                        imported_df.loc[19]["Pipeline Diameter"],
                        imported_df.loc[19]["Pipeline Length"],
                        imported_df.loc[19]["p2"],
                        imported_df.loc[19]["p4"],
                        imported_df.loc[19]["p6"],
                        imported_df.loc[19]["p8"],
                        imported_df.loc[19]["p10"],
                        imported_df.loc[19]["p12"])
#print(experiment_tuple)
import time
  
# Timer starts
starttime = time.time()
# Minimize objective function using SLSQP
result = minimize(objective_function.experiment, experiment_tuple, method='SLSQP', bounds=bnds)#, constraints=cons)
slsqp_laptime = round((time.time() - starttime), 2)
# print(result)
# Minimize objective function using PSO. 
slsqpTime = time.time()
xopt, fopt = pso(objective_function.experiment, lb, ub, swarmsize=100, omega=0.5, phip=0.5, 
    phig=0.5, maxiter=5, minstep=1e-8, minfunc=1e-8, debug=False)
pso_laptime = round((time.time() - slsqpTime), 2)
#Below prints the results of the PSO and SLSQP optimization. We can then manually compare results. 
print("PSO Optimizatoin Results:")
print("xopt: ", xopt)
print("fopt: ", fopt)

print("SLSQP Optimization Results:")
print(result)

print("Time to complete SLSQP optimization: ", slsqp_laptime, " seconds")
print("Time to complete PSO optimization: ", pso_laptime, " seconds")