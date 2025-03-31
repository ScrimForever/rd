from binary_search import bin_search
import pytest


def test_bin_search_true():
    assert bin_search([1,2,3,4,5,6,7,8,9,10], 5) == 4

def test_bin_search_not_exist():
    assert bin_search([1,2,3,4,5,6,7,8,9,10], 11) == -1

