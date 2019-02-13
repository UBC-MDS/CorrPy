## Test for corr_plus.py

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
rm_x = [1,2,3,4,6,7]
rm_y = [2,3,4,5,1,3]

# Return Error if wrong type
def test_type():
    with pytest.raises(TypeError):
        CorrPy.corr_plus(mix_type_x,mix_type_y) # expect ERROR if the input are not numeric
        CorrPy.corr_plus(mix_type_x,multi_y_plus) # expect ERROR if the length of two vectors are different

# The output length should be 1
def test_length():
    assert CorrPy.corr_plus(single_x, single_y) == None # expect None if the length of both vectors are one
    assert isinstance(CorrPy.corr_plus(multi_x,mix_type_y), (float, int, complex)) # output should be a number

# Return Error if one of the input is zero
def test_zero():
    with pytest.raises(TypeError):
        CorrPy.corr_plus(zeros_x, pos_neg_y) # fail if the input is zero vector

# Test if it can calculate the right value
def test_value():
    # deal with negative numbers
    assert round(CorrPy.corr_plus(pos_neg_x, pos_neg_y),5) == round(np.corrcoef(pos_neg_x, pos_neg_y)[0,1],5) 
    # can deal with large numbers
    assert round(CorrPy.corr_plus(large_x, large_y),5) == round(np.corrcoef(large_x, large_y)[0,1],5) 
    # can deal with missing values
    assert CorrPy.corr_plus(missing_x, missing_x) == 1 
    assert round(CorrPy.corr_plus(missing_x, missing_y),5) == round(np.corrcoef(rm_x, rm_y)[0,1],5)
