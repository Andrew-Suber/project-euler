"""Basic tests for functions in project euler library."""

import pytest
import lib_project_euler as lpe


def test_validate_integers():
    """Test function validate_integers."""
    pytest.raises(TypeError, lpe.validate_integers, 'abc')
    pytest.raises(TypeError, lpe.validate_integers, 4.1)
    pytest.raises(TypeError, lpe.validate_integers, 'abc', 22)
    pytest.raises(TypeError, lpe.validate_integers, 'abc', 'def', 'ghi')
    assert lpe.validate_integers(4) is None
    assert lpe.validate_integers(8, 2001) is None

def test_fibonacci():
    """Test fibonacci function."""
    assert lpe.fibonacci(4) == 3
    assert lpe.fibonacci(5) == 5
    assert lpe.fibonacci(6) == 8
    assert lpe.fibonacci(7) == 13

def test_prime_sieve():
    """Test prime_sieve function."""
    assert lpe.prime_sieve(20) == {2, 3, 5, 7, 11, 13, 17, 19}

def test_find_prime_factors():
    """Test function find_prime_factors."""
    assert lpe.find_prime_factors(28) == {2, 7}
    assert lpe.find_prime_factors(24) == {2, 3}
    assert lpe.find_prime_factors(49) == {7}
    assert lpe.find_prime_factors(100) == {2, 5}
    assert lpe.find_prime_factors(600851475143) == {1471, 6857, 839, 71}

def test_happy_step():
    """Test function happy_step."""
    assert lpe.happy_step(2) == 4
    assert lpe.happy_step(13) == 10
    assert lpe.happy_step(24) == 20
    assert lpe.happy_step(35) == 34
    assert lpe.happy_step(46) == 52

def test_find_product():
    """Test function find_product."""
    assert lpe.find_product('23') == 6
    assert lpe.find_product('234') == 24
    assert lpe.find_product('526') == 60
    assert lpe.find_product('872') == 112
    assert lpe.find_product('111') == 1

def test_is_pyth_triplet():
    """Test is_pyth_triplet function."""
    assert lpe.is_pyth_triplet(3, 4, 5) is True
    assert lpe.is_pyth_triplet(5, 12, 13) is True
    assert lpe.is_pyth_triplet(18, 24, 30) is True
    assert lpe.is_pyth_triplet(10, 24, 26) is True

def test_find_factors():
    """Test function find_prime_factors."""
    assert lpe.find_factors(28) == {1, 2, 4, 7, 14, 28}
    assert lpe.find_factors(49) == {1, 7, 49}
    assert lpe.find_factors(100) == {1, 2, 4, 5, 10, 20, 25, 50, 100}

def test_add_up_divisors():
    """Test function add_up_divisors."""
    assert  lpe.add_up_divisors(6) == 6
    assert  lpe.add_up_divisors(28) == 28

def test_find_collatz_stopping_time():
    """Test function find_collatz_stopping_time."""
    assert lpe.find_collatz_stopping_time(5) == 6
    assert lpe.find_collatz_stopping_time(9) == 20
    assert lpe.find_collatz_stopping_time(13) == 10
    assert lpe.find_collatz_stopping_time(19) == 21

def test_is_happy():
    """Test function is_happy."""
    assert lpe.is_happy(44) is True
    assert lpe.is_happy(1) is True
    assert lpe.is_happy(100) is True
    assert lpe.is_happy(129) is True
    assert lpe.is_happy(101) is False
    assert lpe.is_happy(498) is False
    assert lpe.is_happy(3973) is False

def test_is_pan_digital():
    """Test function is_pan_digital."""
    assert lpe.is_pan_digital(1) is True
    assert lpe.is_pan_digital(123) is True
    assert lpe.is_pan_digital(1234) is True
    assert lpe.is_pan_digital(54321) is True
    assert lpe.is_pan_digital(615243) is True
    assert lpe.is_pan_digital(987) is False
    assert lpe.is_pan_digital(87654) is False

def test_find_combinations():
    """Test function find_combinations. Source of reference values: calculatorsoup.com"""
    assert lpe.find_combinations(4, 2) == 6
    assert lpe.find_combinations(8, 4) == 70
    assert lpe.find_combinations(10, 3) == 120
    assert lpe.find_combinations(17, 11) == 12376

def test_number_to_word():
    """Test function number_to_word."""
    pytest.raises(ValueError, lpe.number_to_word, 1001)
    assert lpe.number_to_word(18) == "eighteen"
    assert lpe.number_to_word(52) == "fifty-two"
    assert lpe.number_to_word(152) == "one hundred and fifty-two"
    assert lpe.number_to_word(952) == "nine hundred and fifty-two"
    assert lpe.number_to_word(1000) == "one thousand"
    assert lpe.number_to_word(100) == "one hundred"

def test_gcd():
    """Test function gcd."""
    assert lpe.gcd(20, 15) == 5
    assert lpe.gcd(4, 0) == 4
    assert lpe.gcd(7, 13) == 1
    assert lpe.gcd(28851538, 1183019) == 17657

def test_lcm():
    """Test function lcm."""
    assert lpe.lcm(9, 12) == 36
    assert lpe.lcm(98, 102) == 4998
    assert lpe.lcm(48, 118) == 2832
    assert lpe.lcm(35, 95) == 665

def test_create_nine_digit_product():
    """Test function create_nine_digit_product."""
    assert lpe.create_nine_digit_product(9) == "918273645"
    assert lpe.create_nine_digit_product(192) == "192384576"

def test_sum_of_digit_factorial():
    """Test function find_sum_of_digit_factorial."""
    assert lpe.find_sum_of_digit_factorial(123) == 9
    assert lpe.find_sum_of_digit_factorial(292) == 362884

def test_sum_fifth_power_of_digits():
    """Test function sum_fifth_power_of_digits."""
    assert lpe.sum_fifth_power_of_digits(456) == 11925
    assert lpe.sum_fifth_power_of_digits(789) == 108624
    assert lpe.sum_fifth_power_of_digits(123) == 276

def test_find_proper_divisors():
    """Test function find_proper_divisors."""
    assert lpe.find_proper_divisors(28) == {1, 2, 4, 7, 14}
    pytest.raises(ValueError, lpe.find_proper_divisors, 0)

pytest.main(['-v'])
