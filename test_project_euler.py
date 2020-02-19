"""Basic tests for functions in project euler library."""

import lib_project_euler


def test_fibonacci():
    """Test fibonacci function."""
    assert lib_project_euler.fibonacci(4) == 3
    assert lib_project_euler.fibonacci(5) == 5
    assert lib_project_euler.fibonacci(6) == 8
    assert lib_project_euler.fibonacci(7) == 13

def test_prime_sieve():
    """Test prime_sieve function."""
    assert lib_project_euler.prime_sieve(20) == {2, 3, 5, 7, 11, 13, 17, 19}

def test_find_prime_factors():
    """Test function find_prime_factors."""
    assert lib_project_euler.find_prime_factors(28) == {2, 7}
    assert lib_project_euler.find_prime_factors(49) == {7}
    assert lib_project_euler.find_prime_factors(100) == {2, 5}
    assert lib_project_euler.find_prime_factors(600851475143) == {1471, 6857, 839, 71}

def test_happy_step():
    """Test function happy_step."""
    assert lib_project_euler.happy_step(2) == 4
    assert lib_project_euler.happy_step(13) == 10
    assert lib_project_euler.happy_step(24) == 20
    assert lib_project_euler.happy_step(35) == 34
    assert lib_project_euler.happy_step(46) == 52

def test_find_product():
    """Test function find_product."""
    assert lib_project_euler.find_product('23') == 6
    assert lib_project_euler.find_product('234') == 24
    assert lib_project_euler.find_product('526') == 60
    assert lib_project_euler.find_product('872') == 112
    assert lib_project_euler.find_product('111') == 1

def test_is_pyth_triplet():
    """Test is_pyth_triplet function."""
    assert lib_project_euler.is_pyth_triplet(3, 4, 5) is True
    assert lib_project_euler.is_pyth_triplet(5, 12, 13) is True
    assert lib_project_euler.is_pyth_triplet(18, 24, 30) is True
    assert lib_project_euler.is_pyth_triplet(10, 24, 26) is True

def test_find_factors():
    """Test function find_prime_factors."""
    assert lib_project_euler.find_factors(28) == {1, 2, 4, 7, 14, 28}
    assert lib_project_euler.find_factors(49) == {1, 7, 49}
    assert lib_project_euler.find_factors(100) == {1, 2, 4, 5, 10, 20, 25, 50, 100}
