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
    assert lpe.validate_integers(8, 2_001) is None

def test_fibonacci():
    """Test fibonacci function."""
    assert lpe.fibonacci(0) == 0
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
    assert lpe.find_prime_factors(600_851_475_143) == {1_471, 6_857, 839, 71}
    pytest.raises(ValueError, lpe.find_prime_factors, 0)

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
    assert lpe.is_happy(3_973) is False

def test_is_pan_digital():
    """Test function is_pan_digital."""
    assert lpe.is_pan_digital(1) is True
    assert lpe.is_pan_digital(123) is True
    assert lpe.is_pan_digital(1_234) is True
    assert lpe.is_pan_digital(54_321) is True
    assert lpe.is_pan_digital(615_243) is True
    assert lpe.is_pan_digital(987) is False
    assert lpe.is_pan_digital(87_654) is False

def test_find_combinations():
    """Test function find_combinations. Source of reference values: calculatorsoup.com"""
    assert lpe.find_combinations(4, 2) == 6
    assert lpe.find_combinations(8, 4) == 70
    assert lpe.find_combinations(10, 3) == 120
    assert lpe.find_combinations(17, 11) == 12_376

def test_number_to_word():
    """Test function number_to_word."""
    pytest.raises(ValueError, lpe.number_to_word, 1_001)
    pytest.raises(ValueError, lpe.number_to_word, 0)
    assert lpe.number_to_word(18) == "eighteen"
    assert lpe.number_to_word(52) == "fifty-two"
    assert lpe.number_to_word(152) == "one hundred and fifty-two"
    assert lpe.number_to_word(952) == "nine hundred and fifty-two"
    assert lpe.number_to_word(1000) == "one thousand"
    assert lpe.number_to_word(100) == "one hundred"

def test_greatest_common_divisor():
    """Test function greatest_common_divisor."""
    assert lpe.greatest_common_divisor(20, 15) == 5
    assert lpe.greatest_common_divisor(4, 0) == 4
    assert lpe.greatest_common_divisor(7, 13) == 1
    assert lpe.greatest_common_divisor(28_851_538, 1_183_019) == 17_657

def test_lowest_common_multiple():
    """Test function lowest_common_multiple."""
    assert lpe.lowest_common_multiple(9, 12) == 36
    assert lpe.lowest_common_multiple(98, 102) == 4_998
    assert lpe.lowest_common_multiple(48, 118) == 2_832
    assert lpe.lowest_common_multiple(35, 95) == 665

def test_create_nine_digit_product():
    """Test function create_nine_digit_product."""
    assert lpe.create_nine_digit_product(9) == "918273645"
    assert lpe.create_nine_digit_product(192) == "192384576"

def test_sum_of_digit_factorial():
    """Test function find_sum_of_digit_factorial."""
    assert lpe.find_sum_of_digit_factorial(123) == 9
    assert lpe.find_sum_of_digit_factorial(292) == 362_884

def test_sum_fifth_power_of_digits():
    """Test function sum_fifth_power_of_digits."""
    assert lpe.sum_fifth_power_of_digits(456) == 11_925
    assert lpe.sum_fifth_power_of_digits(789) == 108_624
    assert lpe.sum_fifth_power_of_digits(123) == 276

def test_find_proper_divisors():
    """Test function find_proper_divisors."""
    assert lpe.find_proper_divisors(28) == {1, 2, 4, 7, 14}
    assert lpe.find_proper_divisors(1) == set()
    pytest.raises(ValueError, lpe.find_proper_divisors, 0)

def test_num_and_sum_of_div():
    """Test function num_and_sum_of_div."""
    assert lpe.num_and_sum_of_div(220) == {220, 284}
    assert lpe.num_and_sum_of_div(220) == {220, 284}
    pytest.raises(ValueError, lpe.num_and_sum_of_div, 0)

def test_is_perfect():
    """Test function is_perfect."""
    assert lpe.is_perfect(28) is True
    assert lpe.is_perfect(496) is True
    assert lpe.is_perfect(234) is False
    assert lpe.is_perfect(567) is  False
    assert lpe.is_perfect(0) is  False
    assert lpe.is_perfect(1) is  False

def test_is_amicable():
    """Test function is_amicable."""
    assert lpe.is_amicable(220) is True
    assert lpe.is_amicable(284) is True
    assert lpe.is_amicable(1_184) is True
    assert lpe.is_amicable(1_210) is True
    assert lpe.is_amicable(123) is False
    assert lpe.is_amicable(456) is False
    pytest.raises(ValueError, lpe.is_amicable, 0)

def test_is_abundant():
    """Test function is_abundant."""
    assert lpe.is_abundant(24) is True
    assert lpe.is_abundant(30) is True
    assert lpe.is_abundant(40) is True
    assert lpe.is_abundant(25) is False
    assert lpe.is_abundant(35) is False
    assert lpe.is_abundant(45) is False
    pytest.raises(ValueError, lpe.is_abundant, 0)

def test_create_triangle_numbers():
    """Test function create_triangle_numbers."""
    assert lpe.create_triangle_numbers(100) == {0, 1, 66, 3, 36, 6, 10, 45,
                                                78, 15, 21, 55, 91, 28}

def test_create_pentagon_numbers():
    """Test function create_pentagon_numbers."""
    assert lpe.create_pentagon_numbers(100) == {0, 1, 35, 5, 70, 12, 51, 22, 92}

def test_create_hexagon_numbers():
    """Test function create_hexagon_numbers."""
    assert lpe.create_hexagon_numbers(100) == {0, 1, 66, 6, 45, 15, 91, 28}

def test_add_digits():
    """Test function add_digits."""
    pytest.raises(TypeError, lpe.add_digits, 'abc')
    assert lpe.add_digits(123) == 6
    assert lpe.add_digits(0) == 0

def test_create_right_truncations():
    """Test function create_right_truncations."""
    pytest.raises(TypeError, lpe.create_right_truncations, 'abc')
    assert lpe.create_right_truncations(123) == {123, 12, 1}
    assert lpe.create_right_truncations(0) == {0}
    assert lpe.create_right_truncations(54_321) == {54_321, 5_432, 543, 54, 5}
    assert lpe.create_right_truncations(9) == {9}

def test_create_left_truncations():
    """Test function create_left_truncations."""
    pytest.raises(TypeError, lpe.create_left_truncations, 'abc')
    assert lpe.create_left_truncations(123) == {123, 23, 3}
    assert lpe.create_left_truncations(0) == {0}
    assert lpe.create_left_truncations(54321) == {54_321, 4_321, 321, 21, 1}
    assert lpe.create_left_truncations(9) == {9}

def test_get_permutations():
    """Test function get_permutations."""
    assert lpe.get_permutations('abc') == ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']
    assert lpe.get_permutations('') == ['']
    assert lpe.get_permutations('abcd') == ['dcba', 'cdba', 'cbda', 'cbad', 'dbca',
                                            'bdca', 'bcda', 'bcad', 'dbac', 'bdac',
                                            'badc', 'bacd', 'dcab', 'cdab', 'cadb',
                                            'cabd', 'dacb', 'adcb', 'acdb', 'acbd',
                                            'dabc', 'adbc', 'abdc', 'abcd'
                                           ]

def test_find_composites():
    """Test function find_composites."""
    assert lpe.find_composites(20) == {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20}

def test_find_goldbach_numbers():
    """Test function find_goldbach_numbers."""
    assert lpe.find_goldbach_numbers(20) == {4, 5, 7, 9, 10, 11, 13, 15, 19}

def test_equal_division():
    """Test function equal_division."""
    sample = 'abcdefghijklmnopqrstuvwxyz'
    assert lpe.equal_division(sample, 1) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                             'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                                             'y', 'z']
    assert lpe.equal_division(sample, 2) == ['ab', 'cd', 'ef', 'gh', 'ij', 'kl',
                                             'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz']
    assert lpe.equal_division(sample, 3) == ['abc', 'def', 'ghi', 'jkl', 'mno',
                                             'pqr', 'stu', 'vwx']

def test_check_for_pattern():
    """Test function check_for_pattern."""
    assert lpe.check_for_pattern("33333") == 1
    assert lpe.check_for_pattern("12121") == 2
    assert lpe.check_for_pattern("123123") == 3
    assert lpe.check_for_pattern("12345") is False
    assert lpe.check_for_pattern("123456789") is False

def test_get_rotations():
    """Test function get_rotations."""
    assert lpe.get_rotations(1) == {1}
    assert lpe.get_rotations(12) == {21, 12}
    assert lpe.get_rotations(123) == {123, 231, 312}

def test_is_palindrome():
    """Test function is_palindrome."""
    assert lpe.is_palindrome('') is False
    assert lpe.is_palindrome(123) is False
    assert lpe.is_palindrome(232) is True
    assert lpe.is_palindrome(99) is True

def test_is_binary_palindrome():
    """Test function is_binary_palindrome."""
    assert lpe.is_binary_palindrome(3) is True
    assert lpe.is_binary_palindrome(5) is True
    assert lpe.is_binary_palindrome(232) is False
    assert lpe.is_binary_palindrome(99) is True

def test_is_sequence():
    """Test function is_sequence."""
    assert lpe.is_sequence([8, 11, 14, 17]) is True
    assert lpe.is_sequence([2, 3]) is False

def test_is_armstrong():
    """Test function is_armstrong."""
    assert lpe.is_armstrong(370) is True
    assert lpe.is_armstrong(153) is True
    assert lpe.is_armstrong(407) is True
    assert lpe.is_armstrong(1001) is False
    assert lpe.is_armstrong(55) is False

def test_is_permutation():
    """Test function is_permutation."""
    assert lpe.is_permutation(['abc', 'cba']) is True
    assert lpe.is_permutation(['3214', '1234']) is True
    assert lpe.is_permutation(['3215', '1234']) is False
    assert lpe.is_permutation(['33124', '1234']) is False
    assert lpe.is_permutation(['abc', 'cba', 'bac']) is True
    assert lpe.is_permutation(['122', '112']) is False

def test_find_digit_sum():
    """Test function find_digit_sum."""
    assert lpe.find_digit_sum(812) == 11


pytest.main(['-v'])
