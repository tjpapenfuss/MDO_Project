import main as objective_function
import pandas as pd
# from csv import DictReader
import csv
from sensitivity import SensitivityAnalyzer
import matplotlib.pyplot as plt


# Read in the DOE data. This is the initial guess for the PSO optimization
# imported_df = pd.read_csv("./file_import_and_graph/DOE_tanner.csv", index_col=0)

def function_tuple_creator(Number_Wells,Number_Connections,Pipeline_Diameter,Pipeline_Length,p2,p4,p6,p8,p10,p12):
        new_tuple = (Number_Wells,Number_Connections,Pipeline_Diameter,Pipeline_Length,p2,p4,p6,p8,p10,p12)
        print(new_tuple)
        return objective_function.experiment(new_tuple)

csv2dict = pd.read_csv("./file_import_and_graph/DOE_sensitivity.csv", index_col=0).to_dict()
list_dict = list(csv2dict)
# with open("./file_import_and_graph/DOE_sensitivity.csv", 'r') as file:
#     dict_reader = DictReader(file)
     
#     list_of_dict = list(dict_reader)
   
#     print(list_of_dict)

sensitivity_dict = {
    'Number_Wells': [10,20,5],
    'Number_Connections': [1,2,3],
    'Pipeline_Diameter': [4,12,20],
    'Pipeline_Length': [1000,28000,55000],
    'p2': [500,700,900],
    'p4': [900,1300,1800],
    'p6': [2300,2800,3200],
    'p8': [3800,4400,4800],
    'p10': [5000,5500,6000],
    'p12': [6000,6500,7000]
}
# print(csv2dict)
# print(list_dict)
# print(sensitivity_dict)
sa = SensitivityAnalyzer(sensitivity_dict, function_tuple_creator)

plot = sa.plot()
styled_df = sa.styled_dfs()

print(sa.df)
print(styled_df)

sa.df.to_csv('sensitivity_output.csv')

# styled_df.df.to_csv('stylized.csv')