import main as objective_function
import pandas as pd
from scipy.optimize import minimize, dual_annealing

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

# constraints
# 10,000 <= Qinj <= 100,000
# PWH > 0
# PWF > Pres
# Qinj * num_wells * time <= Qmax

bnds = tuple(map(tuple,(bound_num_wells, bound_num_connections, # bound_mass_flow_rate, 
        bound_pipeline_diameter, bound_pipeline_length, bound_p2, 
        bound_p4, bound_p6, bound_p8, bound_p10, bound_p12)))

cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2})

#print(result)


# TO DO: Add in the DOE generation functionality. 
imported_df = pd.read_csv("C:/Users/Stephen Tainter/OneDrive - Massachusetts Institute of Technology/MIT/2023 Spring Classes/16.888/HW/MDO_Project/Assign3/file_import_and_graph/DOE_tanner.csv", index_col=0)
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

#initial guess
x0 = [2,1,1.75,1000, 600, 900, 2800, 3900, 5150, 6900]

# Minimize objective function
result = dual_annealing(objective_function.experiment, x0=x0, bounds=bnds, initial_temp=5000, maxiter=1000)#, constraints=cons)
print(result)
# for index, row in imported_df.iterrows():
#     # Variable initialization from the DOE. 
    
#     NPV,mtot,CAPEX_total = objective_function.experiment(imported_df.loc[index]["Number of Wells"],
#                         imported_df.loc[index]["Number of Connections"],
#                         imported_df.loc[index]["Mass Flow Rate"],
#                         imported_df.loc[index]["Pipeline Diameter"],
#                         imported_df.loc[index]["Pipeline Length"],
#                         imported_df.loc[index]["p2"],
#                         imported_df.loc[index]["p4"],
#                         imported_df.loc[index]["p6"],
#                         imported_df.loc[index]["p8"],
#                         imported_df.loc[index]["p10"],
#                         imported_df.loc[index]["p12"])
#     #Net_Present_Value_Array = [NPV, NPV]
    # npv_array.append(NPV)
    # mtot_array.append(mtot/1000/1000000)
    # capex_array.append(CAPEX_total)
    # #print(imported_df)

npv_array.append(NPV)
# mtot_array.append(mtot/1000/1000000)
# capex_array.append(CAPEX_total)
print(NPV)#, mtot, CAPEX_total)
    #print(imported_df)
# imported_df["NPV"] = npv_array
# imported_df["mtot"] = mtot_array
# imported_df["CAPEX_total"] = capex_array
# imported_df.to_csv("final_df.csv")

