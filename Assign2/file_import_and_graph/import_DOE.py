import pandas as pd

# Import CSV file function. This will import the CSV and return the values that 
# we need to run our model. 
def import_csv(fileName, Run_Id):
    
    #Import the csv files into pandas dataframes.
    df = pd.read_csv(fileName)
    # Must us -1 because Python starts counting at 0
    wellbore_radius = df.loc[Run_Id-1]["Wellbore Radius"] 
    no_wells = df.loc[Run_Id-1]["Number of Wells"]
    return df, wellbore_radius, no_wells

df, radius, no_wells = import_csv("DOE.csv", 1)
print("The wellbore radius is: ", radius)
print("The number of wells is: ", no_wells)



# Testing below, DO NOT USE


# ------------------------------------------------------------------------------------------------------------------ #
# Import from folders
# ------------------------------------------------------------------------------------------------------------------ #
# some_file.py
# import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# sys.path.insert(1, './file_import_and_graph/')

# import import_DOE

# df, radius, no_wells = import_DOE.import_csv("./file_import_and_graph/DOE.csv", 1)
# print("The wellbore radius is: ", radius)
# print("The number of wells is: ", no_wells)