import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   

imported_df = pd.read_csv("DOE_output.csv")


# Use the below line of code to just plot all points in a scatter plot
imported_df.plot(x="Cost", y="Utility", kind="scatter")

# Use this for loop to plot only if some condition is met. 
# Currently the condition is if K3 is set. 
# for index, row in imported_df.iterrows():
#     if(row['K'] == 'K3'):
#         plt.scatter(row['Cost'], row['Utility'], color="orange")
#     else:
#         plt.scatter(row['Cost'], row['Utility'], color="lightblue")

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

# Call the pareto_frontier function with your Cost and Utility values from pythonTrade.csv.
X_values, Y_values = pareto_frontier(imported_df["Cost"], imported_df["Utility"], maxX = False, maxY = True)
#print(X_values, Y_values) # Print out to pareto frontier values.

ax = plt.gca()
ax.set_ylim([0, 1]) # Set the y-axis (Utility) limit to 0-1
plt.scatter(X_values, Y_values, c="red")
plt.plot(X_values, Y_values, 'red', linestyle="--") # Then plot the Pareto frontier on top of your scatter plot.
plt.title("Cost vs Utility - MAU Model")
plt.xlabel("Cost ($ Millions)")
plt.text(300000, 0.9, "Utopia", color="gold")
plt.plot(100000, 0.90, marker='*', markersize=30, color="gold")

# Below is sample code to plot specific architectures we may like. Right now it is plotting the first arch.
plt.plot(imported_df["Cost"][0], imported_df["Utility"][0], marker='s', markersize=8, color="purple")
plt.plot(2900000, 0.215, marker='s', markersize=8, color="purple")
plt.text(1300000, 0.20, "First Architecture", color="purple")


plt.savefig('figure.png') # Save the figure to a file
