# Test Calcuation File

# Imports
import pytest
from unittest.mock import patch
from app.operations import Operations
from app.calculation import (
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    Calculation
)

# Test concrete Calculation classes

# Addition with positive scenario
@patch.object(Operations, 'addition')
def test_add_calculation_execute_positive(mock_addition):
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 15.0
    mock_addition.return_value = expected_result
    add_calc = AddCalculation(a, b)
    # Act
    result = add_calc.execute()
    # Assert
    mock_addition.assert_called_once_with(a, b)
    assert result == expected_result

# Addition with negative scenario
@patch.object(Operations, 'addition')
def test_add_calculation_execute_negative(mock_addition):
    # Arrange
    a = 10.0
    b = 5.0
    mock_addition.side_effect = Exception("Addition error")
    add_calc = AddCalculation(a, b)
    # Act
    with pytest.raises(Exception) as exc_info:
        add_calc.execute()
    # Assert
    assert str(exc_info.value) == "Addition error"

# Subtraction with positive scenario
@patch.object(Operations, 'subtraction')
def test_subtract_calculation_execute_positive(mock_subtraction):
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 5.0
    mock_subtraction.return_value = expected_result
    subtract_calc = SubtractCalculation(a, b)
    # Act
    result = subtract_calc.execute()
    # Assert
    mock_subtraction.assert_called_once_with(a, b)
    assert result == expected_result

# Subtraction with negative scenario
@patch.object(Operations, 'subtraction')
def test_subtract_calculation_execute_negative(mock_subtraction):
    # Arrange
    a = 10.0
    b = 5.0
    mock_subtraction.side_effect = Exception("Subtraction error")
    subtract_calc = SubtractCalculation(a, b)
    # Act
    with pytest.raises(Exception) as exc_info:
        subtract_calc.execute()
    #Assert
    assert str(exc_info.value) == "Subtraction error"

# Multiplication with positive scenario
@patch.object(Operations, 'multiplication')
def test_multiply_calculation_execute_positive(mock_multiplication):
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 50.0
    mock_multiplication.return_value = expected_result
    multiply_calc = MultiplyCalculation(a, b)
    # Act
    result = multiply_calc.execute()
    # Assert
    mock_multiplication.assert_called_once_with(a, b)
    assert result == expected_result

# Multiplication with negative scenario
@patch.object(Operations, 'multiplication')
def test_multiply_calculation_execute_negative(mock_multiplication):
    # Arrange
    a = 10.0
    b = 5.0
    mock_multiplication.side_effect = Exception("Multiplication error")
    multiply_calc = MultiplyCalculation(a, b)
    # Act
    with pytest.raises(Exception) as exc_info:
        multiply_calc.execute()
    # Assert
    assert str(exc_info.value) == "Multiplication error"

# Division with positive scenario
@patch.object(Operations, 'division')
def test_divide_calculation_execute_positive(mock_division):
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 2.0
    mock_division.return_value = expected_result
    divide_calc = DivideCalculation(a, b)
    # Act
    result = divide_calc.execute()
    # Assert
    mock_division.assert_called_once_with(a, b)
    assert result == expected_result

# Division with negative scenario
@patch.object(Operations, 'division')
def test_divide_calculation_execute_negative(mock_division):
    # Arrange
    a = 10.0
    b = 5.0
    mock_division.side_effect = Exception("Division error")
    divide_calc = DivideCalculation(a, b)
    # Act
    with pytest.raises(Exception) as exc_info:
        divide_calc.execute()
    # Assert
    assert str(exc_info.value) == "Division error"

