## Wilson Deng
## Feb 11th, 2019
## `corr_plus` function coefficients calculates the relationship between
## two variables as well as the magnitude of this relationship.

import numpy as np

def corr_plus(var1, var2):
    '''
    calculate the Pearson correlation coefficient between
    two variables using complete case analysis that excludes all observations
    that have NA for at least one variable.

    parameters:
    -----------
    var1 (list): a list or an array of the first random variable
    var2 (list): a list or an array of the second random variable

    Return:
    -------
    corr (number): a single value correlation between two variables
    '''
    # Check input type
    if isinstance(var1, (list, tuple, np.ndarray)) and isinstance(var2, (list, tuple, np.ndarray)):
        var1 = np.array(var1)
        var2 = np.array(var2)
    else:
        raise ValueError("Invalid data input")

    length_1 = len(var1)
    length_2 = len(var2)

    # Check input lengths
    if length_1 != length_2:
        raise ValueError("Input should be equal")

    # return None if two single input
    if length_1 == length_2 == 1:
        return None

    # Remove the pair if there is NaN or Inf
    idx_del = []
    for i in range(len(var1)):
        if np.isnan(var1[i]) or np.isnan(var2[i]) or np.isinf(var1[i]) or np.isinf(var2[i]):
            idx_del.append(i)
    var1 = np.delete(var1,idx_del)
    var2 = np.delete(var2,idx_del)

    # Raise Error if zero vector
    if (var1 == 0).all() or (var2 == 0).all():
        raise TypeError("Input cannot be zero vector")

    # Calculate means
    mean_var1 = var1.mean()
    mean_var2 = var2.mean()

    # Calculate sds
    sd_var1 = np.sqrt(np.mean(abs(var1 - mean_var1)**2))
    sd_var2 = np.sqrt(np.mean(abs(var2 - mean_var2)**2))

    # Calculate Correlation coefficient
    corr = ((var1 - mean_var1)*(var2 - mean_var2)).mean() / (sd_var1*sd_var2)

    return corr
