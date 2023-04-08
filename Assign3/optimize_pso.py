import main as objective_function
import pandas as pd
from scipy.optimize import minimize

# Bounds and constraints (see scipy.optimize.minimize documentation)
# The following variables are used in the objective function:
# number of wells, bounds = (5,20)
bound_num_wells = (5,20)
# num point connections, bounds = (1, 3)
bound_num_connections = (1,3)
# mass flow rate, bounds = (1, 15)
# bound_mass_flow_rate = (1,1)
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
from pyswarm import pso


# constraints
# 10,000 <= Qinj <= 100,000
# PWH > 0
# PWF > Pres
# Qinj * num_wells * time <= Qmax

bnds = (bound_num_wells, bound_num_connections, # bound_mass_flow_rate, 
        bound_pipeline_diameter, bound_pipeline_length, bound_p2, 
        bound_p4, bound_p6, bound_p8, bound_p10, bound_p12)
lb = [bound_num_wells[0], bound_num_connections[0], # bound_mass_flow_rate[0],
        bound_pipeline_diameter[0], bound_pipeline_length[0], bound_p2[0],
        bound_p4[0], bound_p6[0], bound_p8[0], bound_p10[0], bound_p12[0]]
ub = [bound_num_wells[1], bound_num_connections[1], # bound_mass_flow_rate[1],
        bound_pipeline_diameter[1], bound_pipeline_length[1], bound_p2[1],
        bound_p4[1], bound_p6[1], bound_p8[1], bound_p10[1], bound_p12[1]]
cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2})


#print(result)



# TO DO: Add in the DOE generation functionality. 
imported_df = pd.read_csv("./file_import_and_graph/DOE_tanner.csv", index_col=0)
npv_array = []
mtot_array = []
capex_array = []
experiment_tuple = (imported_df.loc[0]["Number of Wells"],
                        imported_df.loc[0]["Number of Connections"],
                        # imported_df.loc[1]["Mass Flow Rate"],
                        imported_df.loc[0]["Pipeline Diameter"],
                        imported_df.loc[0]["Pipeline Length"],
                        imported_df.loc[0]["p2"],
                        imported_df.loc[0]["p4"],
                        imported_df.loc[0]["p6"],
                        imported_df.loc[0]["p8"],
                        imported_df.loc[0]["p10"],
                        imported_df.loc[0]["p12"])
print(experiment_tuple)
#NPV,mtot,CAPEX_total = objective_function.experiment(experiment_tuple)
NPV = objective_function.experiment(experiment_tuple)

# Minimize objective function
result = minimize(objective_function.experiment, experiment_tuple, method='SLSQP', bounds=bnds)#, constraints=cons)
print(result)
xopt, fopt = pso(objective_function.experiment, lb, ub, swarmsize=100, omega=0.5, phip=0.5, phig=0.5, maxiter=100, minstep=1e-8,
    minfunc=1e-8, debug=False)
print("PSO Optimizatoin Results:")
print("xopt: ", xopt)
print("fopt: ", fopt)
print("SLSQP Optimization Results:")
print(result)
