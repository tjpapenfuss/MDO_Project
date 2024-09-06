import main as objective_function
import pandas as pd
import numpy as np
from scipy.optimize import minimize

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
j = 0
experiment_tuple = (imported_df.loc[j]["Number of Wells"],#*5.07000815e-03,
                        imported_df.loc[j]["Number of Connections"],#*2.09854813e-03,
                        imported_df.loc[j]["Pipeline Diameter"],#*1.51650258e-02 ,
                        imported_df.loc[j]["Pipeline Length"],#*1.67625952e+00 ,
                        imported_df.loc[j]["p2"],#*2.45485403e+02,
                        imported_df.loc[j]["p4"],#*2.30389421e-01 ,
                        imported_df.loc[j]["p6"],#*1.17704220e+00 ,
                        imported_df.loc[j]["p8"],#*1.17651883e+00 ,
                        imported_df.loc[j]["p10"],#*2.03766903e+00,
                        imported_df.loc[j]["p12"])#*1.72314951e+00)
print(experiment_tuple)

#et = list(experiment_tuple)
#etar = np.array(et)


# Minimize objective function.
#result = minimize(objective_function.experiment, experiment_tuple, method='SLSQP', bounds=bnds)
#print(result)

## pass in fixed input tuple, add a small perturubation to the tuple, then output the npv, record the npv. All of this can be done in a 10x1 []
tuple_list = list(experiment_tuple)
tuple_listf=tuple_list
tuple_listb=tuple_list
NPV_forward = []
NPV_backward = []
hessian = []
NPV_x0 = [2*(objective_function.experiment(experiment_tuple)) for i in range(10)]
##slope forward
for index,item in enumerate(tuple_list): #count along the 10 rows (or 10 design vars)

       p = 0.01
       tuple_listf[index] = tuple_list[index]+p
       perturb_tuple = tuple(tuple_listf)
       NPV_forward.append(objective_function.experiment(perturb_tuple))
       
       p = 0.01
       tuple_listb[index] = tuple_list[index]-p
       perturb_tuple = tuple(tuple_listb)
       NPV_backward.append(objective_function.experiment(perturb_tuple))
       hessian.append((NPV_backward[index]+NPV_forward[index]-NPV_x0[index])/(p**2)+ p**2/6)
#n = 5
#hessian = hessian[n:]
print("npvx", NPV_x0)
print("npvf", NPV_forward)
print("npvb", NPV_backward)
print("hess", hessian)

L_1 = 1/((abs(np.array(hessian)))**0.5)
print("L 1 ", L_1)