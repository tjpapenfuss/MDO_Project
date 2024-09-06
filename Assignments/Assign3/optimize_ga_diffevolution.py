import main as objective_function
import pandas as pd
from scipy.optimize import differential_evolution

# Bounds and constraints (see scipy.optimize.differential_evolution documentation)
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
bnds = (bound_num_wells, bound_num_connections, 
         bound_pipeline_diameter, bound_pipeline_length, bound_p2, 
          bound_p4, bound_p6, bound_p8, bound_p10, bound_p12)

#imported_df = pd.read_csv("./file_import_and_graph/DOE_tanner.csv", index_col=0)
npv_array = []
#mtot_array = []
#capex_array = []
experiment_tuple = (5,2,12,28000,700,1800,3200,4800,5500,7000)

NPV = objective_function.experiment(experiment_tuple)

# Minimize objective function
result = differential_evolution(objective_function.experiment, maxiter=1000, popsize=500, x0=experiment_tuple, bounds=bnds)
# 
print(result)

#npv_array.append(NPV)
#print(NPV)
    #print(imported_df)
# imported_df["NPV"] = npv_array
# imported_df["mtot"] = mtot_array
# imported_df["CAPEX_total"] = capex_array
# imported_df.to_csv("final_df.csv")
