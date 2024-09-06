##############################################################################################################################
# This file is the model for our group's system. 
# This code was created for 16.888 Multi-Diciplinary Design Optimization.
# Authors: Tanner Papenfuss, Brooke DiMartino, Stephen Tainter, John Beilstein, and Warren Anderson
##############################################################################################################################
import pandas as pd

# Import the architectures and options data frames.
df = pd.read_csv("architectures.csv")
option_df = pd.read_csv("options.csv", index_col=0)
# Set the global Variables. These metrics need to be updated in both architectures.csv and options.csv!
metric1 = "Metric1"
metric2 = "Metric2"
metric3 = "Metric3"
metric4 = "Metric4"
metric5 = "Metric5"
metric6 = "Metric6"


##############################################################################################################################
# The following block of code loops through the data Architectures data frame.
##############################################################################################################################
for item in range(len(df)):
    # The following code gets the ID (Ie. A2.) for the 10 decisions of the system.
    # A1/2 are the options for the first architectural decision D1. 
    #print(a,b,c,d,e,f,g,h,j,k)
    depth = df["D"][item]
    compressor_size = df["C"][item]
    well_spacing = df["W"][item]
    distance_source = df["S"][item]
    porosity = df["P"][item]

    ##############################################################################################################################
    # The following block of code is setting the utility values.
    # These utilities are calculated according to the following formulas:
    # U_f=  (2D1+D3+D5 )/4
    # U_A=  (D1+D2+D6+D8 )/4
    # U_I=  (D1+D2+D4+2D7+D9)/6
    # U_T=  (D1+D2+D4+3D6+2D7+2D10)/10
    # U_S=  (D1+D3+5D10 )/7
    # U_H=  (D1+D10 )/2
    # Where D is the decision identifier. Ie. D1 is Measurement collection architecture decision. 
    ##############################################################################################################################
    # A block of code
    # Set the Utility value for the Frequency.
    #df["Frequency"][item] = ((2*option_df.loc[a_val]["Frequency"]) + \
    #                        option_df.loc[c_val]["Frequency"] + \
    #                        option_df.loc[d_val]["Frequency"]) / 4
    df.at[item, metric1] = round(((2*option_df.loc[depth][metric1]) + \
                            option_df.loc[compressor_size][metric1]) / 3, 2)

    # Set the Utility value for the Accuracy.
    df.at[item,metric2] = round((option_df.loc[depth][metric2] + \
                            option_df.loc[well_spacing][metric2] + \
                            option_df.loc[porosity][metric2]) / 3, 2)
    #print(option_df.loc[a_val]["Accuracy"], option_df.loc[b_val]["Accuracy"], option_df.loc[f_val]["Accuracy"], option_df.loc[h_val]["Accuracy"])

    # Set the Utility value for the Innovation.
    # df.at[item,metric3] = round((option_df.loc[depth]["Innovation"] + \
    #                         option_df.loc[b_val]["Innovation"] + \
    #                         option_df.loc[d_val]["Innovation"] + \
    #                         option_df.loc[j_val]["Innovation"] + \
    #                         (2*option_df.loc[g_val]["Innovation"])) / 6, 2)
    
    # # Set the Utility value for the Setup time.
    # df.at[item,metric4] = round((option_df.loc[depth]["Setup time"] + \
    #                         option_df.loc[b_val]["Setup time"] + \
    #                         option_df.loc[d_val]["Setup time"] + \
    #                         (3*option_df.loc[f_val]["Setup time"]) + \
    #                         (2*option_df.loc[g_val]["Setup time"]) + \
    #                         (2*option_df.loc[k_val]["Setup time"])) / 10, 2)

    # # Set the Utility value for the Safety.
    # df.at[item,metric5] = round((option_df.loc[depth]["Safety"] + \
    #                         option_df.loc[c_val]["Safety"] + \
    #                         (5*option_df.loc[k_val]["Safety"])) / 7, 2)

    # # Set the Utility value for the Judgement.
    # df.at[item,metric6] = round((option_df.loc[depth]["Judgement"] + \
    #                         option_df.loc[k_val]["Judgement"]) / 2, 2)


    # Set value for the Cost. 
    df.at[item,"Cost"] = round((option_df.loc[depth]["Cost"] + \
                            option_df.loc[compressor_size]["Cost"] + \
                            option_df.loc[well_spacing]["Cost"] + \
                            option_df.loc[porosity]["Cost"] + \
                            option_df.loc[distance_source]["Cost"]) / 5, 2)
    

df.to_csv("outputTesting.csv")