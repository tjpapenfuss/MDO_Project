# This file takes in the DOE, runs the main.py experiment function to generate 
# outputs. These outputs are fed into the trade_space.py file. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   
import experiment_tanner as objective_function

# Open up the Experiment DF. 
imported_df = pd.read_csv("experiment_output_NPV.csv")

# Run the experiment DOE through the experiment. This will output a DOE with 
# NPV and total CO2 generated. 
NPV_array = []
Total_CO2_Gen = []
for index, row in imported_df.iterrows():
    experiment_tuple = (imported_df.loc[index]["Number of Wells"],
                        imported_df.loc[index]["Number of Connections"],
                        imported_df.loc[index]["Pipeline Diameter"],
                        imported_df.loc[index]["Pipeline Length"],
                        imported_df.loc[index]["p2"],
                        imported_df.loc[index]["p4"],
                        imported_df.loc[index]["p6"],
                        imported_df.loc[index]["p8"],
                        imported_df.loc[index]["p10"],
                        imported_df.loc[index]["p12"])
    output = objective_function.experiment(experiment_tuple)
    if(output[0] > 0 and output[1] > 0):
        NPV_array.append(output[0])
        Total_CO2_Gen.append(output[1]/1000000)

print("Printing NPV and CO2Gen")
print(NPV_array)
print(Total_CO2_Gen)
# Use the below line of code to just plot all points in a scatter plot
plt.scatter(NPV_array, Total_CO2_Gen, color="lightblue")
#plt.show()

def pareto_frontier(Xs, Ys, maxX = True, maxY = True):
    # Sort the list in either ascending or descending order of X
    myList = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxX)
    # Start the Pareto frontier with the first value in the sorted list
    p_front = [myList[0]]    
    # Loop through the sorted list
    for pair in myList[1:]:
        if maxY:
            if pair[1] >= p_front[-1][1]: # Look for higher values of Y…
                p_front.append(pair) # … and add them to the Pareto frontier
                print(pair)
        else:
            if pair[1] <= p_front[-1][1]: # Look for lower values of Y…
                p_front.append(pair) # … and add them to the Pareto frontier
                print(pair)
    # Turn resulting pairs back into a list of Xs and Ys
    p_frontX = [pair[0] for pair in p_front]
    p_frontY = [pair[1] for pair in p_front]
    return p_frontX, p_frontY

# Call the pareto_frontier function with your NPV and mtot values from pythonTrade.csv.
X_values, Y_values = pareto_frontier(NPV_array, Total_CO2_Gen, maxX = True, maxY = False)
#print(X_values, Y_values) # Print out to pareto frontier values.

ax = plt.gca()
# ax.set_ylim([0, 1]) # Set the y-axis (mtot) limit to 0-1
plt.scatter(X_values, Y_values, c="red")
plt.plot(X_values, Y_values, 'red', linestyle="--") # Then plot the Pareto frontier on top of your scatter plot.
plt.title("NPV vs mtot - MAU Model")
plt.xlabel("NPV ($ Millions)")

# plt.text(300000, 0.9, "Utopia", color="gold")
# plt.plot(100000, 0.90, marker='*', markersize=30, color="gold")

# # Below is sample code to plot specific architectures we may like. Right now it is plotting the first arch.
# plt.plot(NPV_array[0], Total_CO2_Gen[0], marker='s', markersize=8, color="purple")
# plt.plot(2900000, 0.215, marker='s', markersize=8, color="purple")
# plt.text(1300000, 0.20, "First Architecture", color="purple")


plt.savefig('figure.png') # Save the figure to a file
