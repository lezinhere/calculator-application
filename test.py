# test.py

import pytest
from app import add, subtract, multiply, divide

def test_add():
    """Test the add function with various examples."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -3) == -8

def test_subtract():
    """Test the subtract function with various examples."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0
    assert subtract(10, 2) == 8

def test_multiply():
    """Test the multiply function with various examples."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0
    assert multiply(-2, -3) == 6

def test_divide():
    """Test the divide function with various examples."""
    assert divide(6, 3) == 2
    assert divide(10, 2) == 5
    assert divide(-8, 4) == -2
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(5, 0)

if __name__ == "__main__":
    # Simple test runner for when pytest is not available
    try:
        test_add()
        test_subtract()
        test_multiply()
        test_divide()
        test_divide_by_zero()
        print("All tests passed!")
    except Exception as e:
        print(f"Test failed: {e}")
