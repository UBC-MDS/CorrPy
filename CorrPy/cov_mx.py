import numpy as np

def cov_mx(m):
    '''
    calculates the covariance matrix of the two variables and
    automatically deals with the missing value

    parameters:
    -----------
    matrix m (2D np.array): a matrix that contains one or more than one random variable.
                            Each row stands for each variables.
    Return:
    -------
    cov_matrix c (2D np.array): a matrix that contains the covariance
        between random variables in the input matrix
    '''

    # check whether the input is valid or not
    m = np.asarray(m)
    if m.ndim == 1:
        raise TypeError("Input should be a 2D array")
    # elif m.ndim > 2:
    #     raise TypeError("m has more than 2 dimensions")
    # raise exception when the input dimensions is more than 2
    try:
        if m.ndim > 2:
            raise Exception()
    except:
        raise TypeError("m has more than 2 dimensions")


    # convert the input to a valid matrix (2D array)
    m = np.array(m, ndmin=2)
    if m.size == 2:
        return None

    # remove inf and nan values
    mask = np.any(np.isnan(m) | np.isinf(m), axis=1)
    m = m[~mask]

    # check if the matrix is empty after removing inf and nan
    if m.size == 0:
        return None

    # calculate covariance matrix
    X = m.copy()
    X = X.T
    N = X.shape[0]
    X = X - X.mean(axis = 0)
    C = np.dot(X.T, X.conj()) / (N-1) # degree of freedom

    return C
