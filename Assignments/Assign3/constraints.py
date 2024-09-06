def sys_constraint(inputs):
    #return value must come back as 0 to be accepted
    #if return value is anything other than 0 it's rejected
    #as not a valid answer.
    total = 50.0 - np.sum(inputs)
    return total