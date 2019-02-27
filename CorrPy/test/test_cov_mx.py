# Test for cov_mx.py
import os
import sys
sys.path.insert(0, os.path.abspath("../../CorrPy"))
import numpy as np
import pytest
import CorrPy

# create some fake variables
single_x = [11]
single_y = [22]
zeros_x = [0,0,0,0]
positive_negative_x = [1,-2,3,-4]
positive_negative_y = [-6,7,-8,9]
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

def test_type():
    '''test if the input is in a valid format'''
    with pytest.raises(TypeError):
        CorrPy.cov_mx(single_x) # fail if only single value
    with pytest.raises(TypeError):
        CorrPy.cov_mx(np.array([mix_type_x,mix_type_y])) # fail if wrong type
    with pytest.raises(TypeError):
        CorrPy.cov_mx(positive_negative_x) # fail if it is 1D array

def test_output():
    '''test if the output is in a valid format'''
    # return None if two inputs contains only a single value individually
    assert CorrPy.cov_mx(np.array([single_x, single_y])) == None
    # the row and column of the output should match
    assert np.shape(CorrPy.cov_mx(matrix_full))[0] == np.shape(CorrPy.cov_mx(matrix_full))[1]
    # using pair wise complete so the shape is deducted
    assert np.shape(CorrPy.cov_mx(matrix_missing)) == (4,4)

def test_value():
    '''test the correctness of the output'''
    # test the correctness of the output if a input is a 2D array
    assert (CorrPy.cov_mx(matrix_full) == np.ones((5,5))*2.5).all()
    # test the correctness of the output if a input contains NA
    assert (CorrPy.cov_mx(matrix_missing) == np.ones((4,4))*2.5).all()
    # test the correctness of the output if a input contains a combination of positive and negative values
    assert (CorrPy.cov_mx(np.array([positive_negative_x, positive_negative_y])) == np.cov(np.array([positive_negative_x, positive_negative_y]))).all()
    # test the correctness of the output if a input contains large numbers
    assert (CorrPy.cov_mx(np.array([large_x, large_y])) == np.cov(np.array([large_x, large_y]))).all()
    # test the correctness of the output if a input contains zero vector
    assert (CorrPy.cov_mx(np.array([zeros_x, positive_negative_y])) == np.cov(np.array([zeros_x, positive_negative_y]))).all()
