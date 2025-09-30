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

