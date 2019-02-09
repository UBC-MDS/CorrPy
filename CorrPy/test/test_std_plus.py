
## inititalization

import numpy as np
import pytest
import corrPy

one_x = [11]
zeros_x = [0,0,0,0]
pos_neg_x = [1,-2,3,-4]
large_x = [1000,-2000,3000]
multi_x = [1,2,3,4,5,6,7]
mix_type_x = [1,"2",3,4,5]
miss_x = [1,2,3,4,5,6,7, np.nan]
bool_x = [True, True, False, True]


# Return Error if input data type is not numeric
def test_type():
    with pytest.raise(TypeError):
        corrPy.std_plus(mix_type_x) # return ERROR if input vector has a string
		corrPy.std_plus(bool_x)# return ERROR if input vector is boolean
 
        
# The output should be of length 1
def test_length():
    assert length(std_plus(multi_x)) == 1 # length of the computed output is 1


# Test the computed values of standard deviation
def test_value():
    assert corrPy.std_plus(one_x) == 0.0 # return zero when input has one element
	assert corrPy.std_plus(pos_neg_x) == 2.692582403567252 # compute standard deviation for input of positive and negative numbers
    assert corrPy.std_plus(large_x) == 2054.8046676563254 # compute standard deviation for large numbers
    assert corrPy.std_plus(miss_x) == corrPy.std_plus(multi_x) # ignore the NA and compute the standard deviation for the rest of the numbers
  	assert corrPy.std_plus(zeros_x) == 0.0