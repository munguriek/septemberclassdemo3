"""
Unit tests for calculator functions.
"""
import pytest
from calculator import add_numbers, multiply_numbers, get_numbers
from unittest.mock import patch


def test_add_numbers_positive():
    """Test addition with positive numbers."""
    assert add_numbers([1, 2, 3]) == 6
    assert add_numbers([10, 20]) == 30


def test_add_numbers_negative():
    """Test addition with negative numbers."""
    assert add_numbers([-1, -2, -3]) == -6
    assert add_numbers([10, -5]) == 5


def test_add_numbers_single():
    """Test addition with single number."""
    assert add_numbers([5]) == 5


def test_add_numbers_empty():
    """Test addition with empty list."""
    assert add_numbers([]) == 0


def test_multiply_numbers_positive():
    """Test multiplication with positive numbers."""
    assert multiply_numbers([2, 3, 4]) == 24
    assert multiply_numbers([5, 2]) == 10


def test_multiply_numbers_with_zero():
    """Test multiplication with zero."""
    assert multiply_numbers([5, 0, 10]) == 0


def test_multiply_numbers_single():
    """Test multiplication with single number."""
    assert multiply_numbers([7]) == 7


def test_multiply_numbers_negative():
    """Test multiplication with negative numbers."""
    assert multiply_numbers([-2, 3]) == -6
    assert multiply_numbers([-2, -3]) == 6


@patch('builtins.input', side_effect=['5', '10', 'done'])
def test_get_numbers_valid(mock_input):
    """Test getting valid numbers from user."""
    result = get_numbers()
    assert result == [5.0, 10.0]


@patch('builtins.input', side_effect=['5', 'abc', '10', 'done'])
def test_get_numbers_with_invalid(mock_input):
    """Test getting numbers with invalid input."""
    result = get_numbers()
    assert result == [5.0, 10.0]