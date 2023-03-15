import pandas as pd

# Import CSV file function. This will import the CSV and return the values that 
# we need to run our model. 
def import_csv(fileName, Run_Id):
    
    # Must us -1 because Python starts counting at 0
    wellbore_radius = df.loc[Run_Id]["Wellbore Radius"] 
    no_wells = df.loc[Run_Id]["Number of Wells"]
    return wellbore_radius, no_wells

#Import the csv files into pandas dataframes.
fileName = "DOE.csv"
df = pd.read_csv(fileName)

# Setup the variables coming from our design vector
well_radius = df["Wellbore Radius"].to_numpy()
no_wells = df["Number of Wells"].to_numpy()
no_connections = df["Number of Connections"].to_numpy()
mass_flow_rate = df["Mass Flow Rate"].to_numpy()
diameter = df["Diameter"].to_numpy()
length = df["Length"].to_numpy()
no_compressors = df["Number of Compressors"].to_numpy()
no_condensers = df["Number of Condensers"].to_numpy()
compressor_outlet_pressure = df["Compressor Outlet Pressure"].to_numpy()
# Stephen thinks we should set the outlet temp to 25C. Make this a parm instead of Design Var.
hx_outlet_tempt = df["HX Outlet Tempt"].to_numpy()

print(well_radius[5])

# An alternative to the above design. We could use the function I defined above to import the values. 
# In this method we would loop everything and import the values as we go. 
index = 0
for item in range(len(df)):
    radius, no_wells = import_csv(fileName, index)
    #print("The wellbore radius is: ", radius)
    #print("The number of wells is: ", no_wells)
    index += 1



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