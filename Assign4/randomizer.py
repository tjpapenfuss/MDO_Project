import main_moo as objective_function
import pandas as pd
from scipy.optimize import minimize
import csv as csv
import random

# Create blank .csv for storing results
# df = pd.DataFrame(list())
# df.to_csv('optimizer_output.csv')

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
for n in range(0, 1000):
        wells = random.randrange(bound_num_wells[0],bound_num_wells[1])
        connections = random.randrange(bound_num_connections[0],bound_num_connections[1])
        diameter = random.randrange(bound_pipeline_diameter[0],bound_pipeline_diameter[1])
        length = random.randrange(bound_pipeline_length[0],bound_pipeline_length[1])
        p2 = random.randrange(bound_p2[0],bound_p2[1])
        p4 = random.randrange(bound_p4[0],bound_p4[1])
        p6 = random.randrange(bound_p6[0],bound_p6[1])
        p8 = random.randrange(bound_p8[0],bound_p8[1])
        p10 = random.randrange(bound_p10[0],bound_p10[1])
        p12 = random.randrange(bound_p12[0],bound_p12[1])
        
        experiment_tuple = (wells,connections,diameter,length,p2,p4,p6,p8,p10,p12)
        print(experiment_tuple)

        # f = open('C:/Users/Beerstein/GitHub/MDO_Project/optimizer_output.csv', 'w')

        # # create the csv writer
        # writer = csv.writer(f)
        # header = ['#_wells,','#_connections','pipe_diam ','pipe_length','p2','p4','p6','p8','p10','p12','npv','capex','utility']

        # # write a row to the csv file
        # writer.writerow(header)

        # # close the file
        # f.close()

        # Minimize objective function.
        result = objective_function.experiment(experiment_tuple)
        print(result)

