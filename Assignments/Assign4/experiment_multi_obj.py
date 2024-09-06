import experiment_tanner as objective_function
import numpy as np

def evalutate_fn(x, out, *args, **kwargs):
    NPV, tot_co2_gen = objective_function.experiment(x)
    
    out["F"] = np.column_stack((NPV, tot_co2_gen))

