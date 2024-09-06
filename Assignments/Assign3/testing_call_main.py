import main as objective_function
import pandas as pd
from scipy.optimize import minimize

# TO DO: Add in the DOE generation functionality. 
imported_df = pd.read_csv("./file_import_and_graph/DOE_tanner.csv", index_col=0)
npv_array = []
mtot_array = []
capex_array = []
for index, row in imported_df.iterrows():
    # Variable initialization from the DOE. 
    
    NPV,mtot,CAPEX_total = objective_function.experiment(imported_df.loc[index]["Injection Tubing Diameter"],
                        imported_df.loc[index]["Number of Wells"],
                        imported_df.loc[index]["Number of Connections"],
                        imported_df.loc[index]["Mass Flow Rate"],
                        imported_df.loc[index]["Pipeline Diameter"],
                        imported_df.loc[index]["Pipeline Length"],
                        imported_df.loc[index]["Number of Compressors"],
                        imported_df.loc[index]["Number of Condensers"],
                        imported_df.loc[index]["Compressor Outlet Pressure"],
                        imported_df.loc[index]["p2"],
                        imported_df.loc[index]["p4"],
                        imported_df.loc[index]["p6"],
                        imported_df.loc[index]["p8"],
                        imported_df.loc[index]["p10"],
                        imported_df.loc[index]["p12"])
    #Net_Present_Value_Array = [NPV, NPV]
    npv_array.append(NPV)
    mtot_array.append(mtot/1000/1000000)
    capex_array.append(CAPEX_total)
    #print(imported_df)
imported_df["NPV"] = npv_array
imported_df["mtot"] = mtot_array
imported_df["CAPEX_total"] = capex_array
imported_df.to_csv("final_df.csv")