import pytest 
from typing import Union

#Import 'Operations' class for testing
from app.operations import Operations

#Numbers can be either integers or floats
Number = Union[int, float]

#Create parametrized testing for addition
@pytest.mark.parametrize(
    "a, b, expected",
    
    [ (2, 3, 5),            #Test adding two positive integers
     (0, 0, 0),             #Test adding two zeros
     (-1, 1, 0),            #Test adding one negative and one positive integer
     (2.5, 3.5, 6.0),       #Test adding two positive floats
     (-2.5, 3.5, 1.0),],     #Test adding one negative float and one positive float
     
     ids=[ "add_two_positive_integers",
          "add_two_zeros",
          "add_negative_and_positive_integer",
          "add_two_positive_floats",
          "add_negative_float_and_positive_float",]
)

#Test addition operation
def test_addition(a: Number, b: Number, expected: Number) -> None:
    result = Operations.addition(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}."
