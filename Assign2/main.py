import nlopt
from numpy import *

import variables

print("The value of CO2 ideal gas constant is: " + str(variables.CO2_IDEAL_GAS_CONST))

#an algorithm (see NLopt Algorithms for possible values) and the dimensionality of the problem (n, the number of optimization parameters).
opt = nlopt.opt(nlopt.NLOPT_GN_DIRECT_L, n=1)
