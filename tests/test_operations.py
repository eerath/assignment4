import pytest 
from typing import Union

#Import 'Operations' class for testing
from app.operations import Operations

#Numbers can be either integers or floats
Number = Union[int, float]

#ADDITION
#Create parametrized testing for addition
@pytest.mark.parametrize(
    "a, b, expected",
    
    [ (2, 3, 5),                #Test adding two positive integers
     (0, 0, 0),                 #Test adding two zeros
     (-1, 1, 0),                #Test adding one negative and one positive integer
     (2.5, 3.5, 6.0),           #Test adding two positive floats
     (-2.5, 3.5, 1.0), ],       #Test adding one negative float and one positive float
     
     ids=[ "add_two_positive_integers",
          "add_two_zeros",
          "add_negative_and_positive_integer",
          "add_two_positive_floats",
          "add_negative_float_and_positive_float",]
)

#Test addition operation
def test_addition(a:Number, b:Number, expected:Number) -> None:
    result = Operations.addition(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}."


#SUBTRACTION
#Create parametrized testing for subtraction
@pytest.mark.parametrize(
    "a, b, expected",

    [ (5, 3, 2),                #Test subtracting two positive integers
     (0, 0, 0),                 #Test subtracting two zeros
     (-5, -3, -2),              #Test subgracting two negative integers
     (10.5, 5.5, 5.0),          #Test subtracting two positive floats
     (-10.5, -5.5, -5.0), ],    #Test subtracting two negative floats

     ids=[ "subctract_two_positive_integers",
          "subtract_two_zeros",
          "subtract_two_negative_integers",
          "subtract_two_positive_floats",
          "subtract_two_negative_floats", ]
)

#Test subtraction operation
def test_subtraction(a:Number, b:Number, expected: Number) -> None:
    result = Operations().subtraction(a, b)
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}."

#MULTIPLICATION
#Create parametrized testing for multiplication
@pytest.mark.parametrize(
    "a, b, expected",

    [ (2, 3, 6),                #Test multiplying two positive integers
     (0, 10, 0),                #Test multiplying by zero
     (-2, -3, 6),               #Test multiplying two negative integers
     (2.5, 4.0, 10.0),          #Test multiplying two positive floats
     (-2.5, 4.0, -10.0), ],     #Test multiplying one positive one negative float

     ids=[ "multiply_two_positive_integers",
          "multiply_by_zero",
          "multiply_two_negative_integers",
          "multiply_two_positive_floats",
          "multiply_one_positive_one_negative_float"],
)

#Test multiplication operation
def test_multiplication(a: Number, b:Number, expected:Number) -> None:
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"

#DIVISION
#Create parametrized testing for division
@pytest.mark.parametrize(
    "a, b, expected",

    [ (6, 3, 2),                #Test dividing two positive integers
     (-6, -3, 2),               #Test dividing two negative integers
     (6.0, 3.0, 2.0),           #Test dividing two positive floats
     (-6.0, 3.0, -2.0),         #Test dividing one positive one negative float
     (0, 5, 0.0), ],            #Test dividing zero by positive integer

     ids=[ "divide_two_positive_integers",
          "divide_two_negative_integers",
          "divive_two_positive_floats",
          "divide_one_positive_one_negative_float",
          "divide_zero_by_positive", ]
)

#Test division operation
def test_division(a:Number, b:Number, expected:Number) -> None:
    result = Operations.division(a, b)
    assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}."

#DIVISION BY ZERO
#Create parametrized testing for division by zero

@pytest.mark.parametrize(
    "a, b",

    [ (1, 0),               #Test dividing by zero with a positive integer
     (-1, 0),               #Test dividing by zero with a negative integer
     (0, 0), ],              #Test dividing zero by zero

     ids=[ "divide_positive_by_zero",
          "divide_negative_by_zero",
          "divide_zero_by_zero", ]
)

#Test division by zero operation
def test_division_by_zero(a:Number, b:Number) -> None:
    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        Operations.division(a, b)

    assert "Division by zero is not allowed." in str(excinfo.value), \
        f"Expected error message 'Division by zero is not allowed.', but got {excinfo.value}."