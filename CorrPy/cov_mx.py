## Wilson Deng
## Feb 8th, 2019
## `cov_mx` function calculates the covariance matrix of the two
## variables and automatically deals with the missing value

import numpy as np

def cov_mx(m):
  '''
  Covariance measures the extent to which corresponding observations
  from two sets of ordered variables vary in a direction.

  parameters:
  -----------
  m (2D np.array): a matrix that contains one or more than one random variable

  Return:
  -------
  cov_matrix (2D np.array): a matrix that contains the covariance between random variables in the input matrix
  '''
  # check whether the input is valid or not 
  m = np.asarray(m)
  if m.ndim > 2:
      raise ValueError("m has more than 2 dimensions")
  
  m = np.array(m, ndmin=2)
  # return Nan if 
  if m.shape[0] == 0: 
      return np.array([]).reshape(0, 0)

  return
