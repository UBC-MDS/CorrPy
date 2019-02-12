import numpy as np

def cov_mx(m):
    '''
    Covariance measures the extent to which corresponding observations
    from two sets of ordered variables vary in a direction.

    parameters:
    -----------
    matrix (2D np.array): a matrix that contains one or more than one random variable

    Return:
    -------
    cov_matrix (2D np.array): a matrix that contains the covariance between random variables in the input matrix
    '''
    
    # check whether the input is valid or not 
    m = np.asarray(m)
    if m.ndim == 1:
        raise TypeError("Input should be a 2D array")
    elif m.ndim > 2:
        raise TypeError("m has more than 2 dimensions")
    
    m = np.array(m, ndmin=2)
    if m.size == 2:
        return None

    # remove inf and nan values
    mask = np.any(np.isnan(m) | np.isinf(m), axis=1)
    m = m[~mask] 
    
    # calculate covariance matrix 
    X = m.copy()
    X = X.T
    N = X.shape[0]
    X = X - X.mean(axis = 0)
    C = np.dot(X.T, X.conj()) / (N-1) # degree of freedom  
    
    return C
