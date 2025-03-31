from multiply_matrices_list import multiply_matrices
import pytest


def test_multiply_matrices_true():
    A = [[1,2], [3,4]]
    B = [[5,6], [7,8]]
    result = multiply_matrices(A, B)
    
    assert result == [[19, 22], [43, 50]]

def test_multiply_matrices_false():
    A = [[1,2], [3,4]]
    B = [[5,6], [7,8]]
    result = multiply_matrices(A, B)
    
    assert result != [[19, 22], [23, 55]]



