## inititalization

import os
import sys
sys.path.insert(0, os.path.abspath("../../CorrPy"))
import numpy as np
import pytest
import CorrPy

single_x = [11]
single_y = [22]
zeros_x = [0,0,0,0]
pos_neg_x = [1,-2,3,-4]
pos_neg_y = [-6,7,-8,9]
large_x = [1000,-2000,3000]
large_y = [-6000,7000,-8000]
multi_x = [1,2,3,4,5]
multi_y = [6,7,8,9,10]
multi_y_plus = [6,7,8,9,10,11]
mix_type_x = [1,"2",3,4,5]
mix_type_y = [1,2,3+2j,4,5]
missing_x = [1,2,3,4,5,6,7, np.nan]
missing_y = [2,3,4,5,np.nan,1,3,4]

matrix_full = np.array(range(25), dtype=float).reshape((5, 5))
matrix_missing = np.array(range(25), dtype=float).reshape((5, 5))
matrix_missing[2,2] = np.nan

# Return Error if wrong type
def test_type():
    with pytest.raises(TypeError):
        CorrPy.cov_mx(single_x) # fail if only single value
        CorrPy.cov_mx(np.array([mix_type_x,mix_type_y])) # fail if wrong type
        CorrPy.cov_mx(pos_neg_x) # fail if it is 1D array

# Test the output shape
def test_length():
    assert CorrPy.cov_mx(np.array([single_x, single_y])) == None # two single value return none
    assert np.shape(cov_mx(matrix_full))[0] == np.shape(cov_mx(matrix_full))[1] # the output shape should match

# Test if it can calculate the right value
def test_missing_value():
    assert np.shape(CorrPy.cov_mx(matrix_missing)) == (4,4) # using pair wise complete so the shape is deducted

# Test if it can calculate the right value
def test_value():
    assert (CorrPy.cov_mx(matrix_full) == np.ones((5,5))*2.5).all() # can deal with 2D array
    assert (CorrPy.cov_mx(matrix_missing) == np.ones((4,4))*2.5).all() # can deal with NA and calculates the right value
    assert (CorrPy.cov_mx(np.array([pos_neg_x, pos_neg_y])) == np.cov(np.array([pos_neg_x, pos_neg_y]))).all() # can deal with 2 1D array inputs
    assert (CorrPy.cov_mx(np.array([large_x, large_y])) == np.cov(np.array([large_x, large_y]))).all() # can deal with large number
    assert (CorrPy.cov_mx(np.array([zeros_x, pos_neg_y])) == np.cov(np.array([zeros_x, pos_neg_y]))).all() # can deal with zero vector
