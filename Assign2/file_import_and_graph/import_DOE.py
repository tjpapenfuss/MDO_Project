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

# df, radius, no_wells = import_csv("DOE.csv", 1)
# print("The wellbore radius is: ", radius)
# print("The number of wells is: ", no_wells)
