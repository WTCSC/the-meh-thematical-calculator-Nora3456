
import pytest
from calculator import addition, subtraction, multiplication, division
import unittest

# Test for addition 
def test_positive_addition():
    """Test 2 positive numbers for addition"""
    assert addition(8, 3) == 11

def test_negative_addition():
    """Test 2 negative numbers for addition"""
    assert addition(-8, -3) == -11

def test_positive_decimals_addition():
    """Test 2 positive decimal numbers for addition"""
    assert addition(8.3, 5.2) == 13.5

# Tests for subtraction
def test_postitive_subtraction():
    """Test 2 positive numbers for subtraction"""
    assert subtraction(8, 3) == 5

def test_negative_subtraction():
    """Test 2 negative numbers for subtraction"""
    assert subtraction(-8, -3) == -5

def test_positive_decimals_subtraction():
    """Test 2 positive decimal numbers for subtraction"""
    assert subtraction(8.3, 5.2) == 3.1

# Tests for multiplication
def test_positive_multiplication():
    """Test 2 positive numbers for multiplication"""
    assert multiplication(8, 5) == 40

def test_negative_and_positive_multiplication():
    """Test 1 positive and 1 negative number for multiplication"""
    assert multiplication(-8, 5) == -40

def test_negative__multiplication():
    """Test 2 negative numbers for multiplication"""
    assert multiplication(-8, -5) == 40

def test_positive_decimals_multiplication():
    """Test 2 positive decimal numbers for multiplication"""
    assert multiplication(8.3, 5.2) == 43.16
    

# Tests for division
def test_positive_division():
    """Test 2 positive numbers for division"""
    assert division(8, 5) == 1.6

def test_postitive_and_negative_division():
    """Test 1 negative and 1 positive number for division"""
    assert division(-8, 5) == -1.6

def test_negative_division():
    """Test 2 negative numbers for division"""
    assert division(-8, -5) == 1.6

def test_0_division():
    """Test 2 positive numbers, one being 0, for division"""
    assert division(8, 0) == ZeroDivisionError


def test_positive_decimals_division():
    """Test 2 positive decimal numbers for division"""
    assert division(8.3, 5.2) == 1.6



