
import numpy as np

def std_plus(x: np.array):
  '''
  Calculates the standard deviation of the values in a numeric vector.
  It is capable of computing standard deviation when the vector contains missing values
  and inifinite values by automatically removing them.

  parameters:
  -----------
  x (array_like) a numeric vector

  Return:
  ------
  sd_value (float): the value of standard deviation of the input data
  '''
  # convert the input vector to numpy array if it is an array-like
  if isinstance(x, (list, tuple, np.ndarray)):
    x = np.array(x)

   # check whether a input vector is valid
  length = len(x)
  if length == 1: # return 0.0 The length of input equals to 1
    return 0.0

  try: # return nan if no input
      x[0]
  except IndexError as detail:
      raise IndexError(str(detail))

  # treat infinite values as missing values and remove them
  x = x[~ np.isinf(x)]

  # remove missing values
  x = x[~ np.isnan(x)]

  # check if an array is empty after we remove inf and nan
  if x.size == 0:
    return np.nan

  # calculate standard deviation
  sd_value = np.sqrt(np.mean(abs(x - x.mean())**2)) # default method in Numpy

  # The following method includes degree of freedom
  # mu = sum(x) / length
  # differences = [i - mu for i in x]
  # sq_differences = [d ** 2 for d in differences]
  # sd_value = np.sqrt(sum(sq_differences) / (length - 1))

  return sd_value
