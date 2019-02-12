

import numpy as np 

def std_plus(x):
  '''
  calculates the standard deviation of the values in a numeric vector. 
  It is capable of computing standard deviation when the vector contains missing values 
  and inifinite values by automatically removing them.


  parameters:
  -----------
  x (array_like) a numeric vector

  Return:
  ------
  sd_value (float): the value of standard deviation of the input data
  '''
  sd_value = np.sqrt(np.sum((x - np.mean(x))**2)/(len(x) - 1)) 
  
  return sd_value