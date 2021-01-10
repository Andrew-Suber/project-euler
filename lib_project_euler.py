"""Library of functions and constants used by Project Euler solutions."""


import math
import string
import pytest


GOLDEN_RATIO = (1 + 5**.05)/2
GOLDEN_RATIO_CONJUGATE = (1 - 5**.05)/2
LOWERCASE_ALPHABET = string.ascii_lowercase


def validate_integers(*nums):
    """Throw type error if any of the arguments are not integers."""
    for num in nums:
        if not isinstance(num, int):
            raise TypeError("Sorry. The function only works with integers.")

def zero_divisors_error(number):
    """Throw value error when listing divisors of zero. Zero has all numbers
    as proper divisors, so it is a special case.
    """
    if number == 0:
        raise ValueError("Zero is a special case.")

def fibonacci(index, cache=None):
    """ Return the Fibbonacci number of n index. Cache results."""
    validate_integers(index)
    if cache is None:
        cache = {0:0, 1:1, 2:1, 3:2,}
    try:
        return cache[index]

    except KeyError:
        pass
    counter = max(cache.keys())
    while counter < index + 1:
        cache[counter] = cache[counter - 1] + cache[counter - 2]
        counter += 1
    return cache[index]

def prime_sieve(limit):
    """Return the set of primes up to the limit."""
    validate_integers(limit)
    square_root = int(limit**.5) + 1
    integers = set(range(2, limit))
    potential_factors = set(range(2, square_root))

    while potential_factors:
        factor = min(potential_factors)
        product = 0
        counter = factor
        while product <= limit:
            product = factor * counter
            integers.discard(product)
            potential_factors.discard(product)
            counter += 1
        potential_factors.discard(factor)
    return integers

def find_composites(limit):
    """Return the set of composite numbers to the limit."""
    validate_integers(limit)
    square_root = int(limit**.5) + 1
    potential_factors = set(range(2, square_root))
    composites = set()

    while potential_factors:
        factor = min(potential_factors)
        product = 0
        counter = factor
        while True:
            product = factor * counter
            if product > limit:
                break
            composites.add(product)
            potential_factors.discard(product)
            counter += 1
        potential_factors.discard(factor)
    return composites

def find_prime_factors(num):
    """Return prime factors of num."""
    validate_integers(num)
    zero_divisors_error(num)
    potential_factor = 2
    prime_factors = set()
    while potential_factor <= num:
        if num % potential_factor == 0:
            prime_factors.add(potential_factor)
            num = num/potential_factor
        else:
            potential_factor += 1
    return prime_factors

def find_product(num):
    """Return the product of a string of digit characters, i.e, '23' produces 6"""
    num = list(num)
    product = 1
    for digit in num:
        product = product * int(digit)
    return product

def is_pyth_triplet(side_a, side_b, hypotenuse_c):
    """Return True if a, b, c compose a Pythagorean triplet."""
    validate_integers(side_a, side_b, hypotenuse_c)
    return (side_a**2) + (side_b**2) == (hypotenuse_c**2)

def find_factors(num):
    """Return factors of num, i.e. 6 returns {1, 2, 3, 6}"""
    validate_integers(num)
    zero_divisors_error(num)
    factors = set()
    for potential_factor in range(1, int(num**.5)+ 1):
        if num % potential_factor == 0:
            factors.add(potential_factor)
            factors.add(int(num/potential_factor))
    return factors

def find_proper_divisors(number):
    """Return a set of proper divisors for number."""
    validate_integers(number)
    results = find_factors(number)
    results.discard(number)
    return results

def add_up_divisors(num):
    """Return sum of proper divisors of num, i.e. 6 returns 1+2+3."""
    validate_integers(num)
    divisors = find_proper_divisors(num)
    return sum(divisors)

def num_and_sum_of_div(number):
    """Return a set consisting of the number and the sum of its
    proper divisors.
    """
    validate_integers(number)
    result = {number}
    result.add(add_up_divisors(number))
    return result

def is_perfect(number):
    """Return true if number is a perfect number i.e. sum of proper
    divisors is equal to number.
    """
    validate_integers(number)
    if number < 1:
        return False

    return len(num_and_sum_of_div(number)) == 1

def is_amicable(number):
    """Return True if number is in an amicable pair, i.e. sum of proper
    divisors of a is equal to b, whose sum of proper divisors is equal to a.
    A perfect number returns False.
    """
    validate_integers(number)
    if is_perfect(number):
        return False

    potential_friend = add_up_divisors(number)
    set_a = num_and_sum_of_div(number)
    set_b = num_and_sum_of_div(potential_friend)
    return set_a == set_b

def is_abundant(number):
    """Return True if the sum of proper divisors is greater than number. I.e,
    24 < 1 + 2 + 3 + 4 + 6 + 8 + 12.
    """
    return number < add_up_divisors(number)

def find_collatz_stopping_time(num):
    """Return the length of the Collatz chain for num.
    12 would return 10 (inclusive of 1).
    """
    validate_integers(num)
    chain_length = 1
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num*3 + 1
        chain_length += 1
    return chain_length

def happy_step(num):
    """Return product of one incrmental step to determine if num is happy/sad.
    i. e., returns the perfect digital invariant of base ten numeral.
    Numeral AB -> A**2 + B**2. 11 -> 2 21 -> 5
    """
    validate_integers(num)
    num = list(str(num))
    total = 0
    for digit in num:
        digit = int(digit)**2
        total = total + digit
    return total

def is_happy(num):
    """Determine if num is happy or sad."""
    validate_integers(num)
    while True:
        if num == 1:
            return True

        if num == 89:
            return False

        num = happy_step(num)

def is_pan_digital(num):
    """Return True if num is pan digital, i.e. 123 or 4,123."""
    comparison = '123456789'
    num = str(num)
    if len(num) > len(set(num)):
        return False

    num = set(num)
    comparison = set(comparison[0:len(num):1])
    return num == comparison

def find_combinations(number, r_items):
    """Return total combinations of n choose r.
    To find the number of combinations for n(number of things you are
    picking from) choose r (number of items you can pick).
    Combinations = n!/r!*(n-r)!
    """
    validate_integers(number, r_items)
    n_fact = math.factorial(number)
    r_fact = math.factorial(r_items)
    n_minus_r_fact = math.factorial(number - r_items)
    result = n_fact/(r_fact*n_minus_r_fact)
    return int(result)

def number_to_word(num):
    """Translate a counting number 1 to 1000 to
    UK English string (uses 'and'), i.e. 1 -> 'one'.
    Internal whitespace and hyphens are present. 152-> one hundred and fifty-two.
    """

    numeral_to_word = {0:"", 1:"one", 2:"two", 3:"three", 4: "four", 5:"five",
                       6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven",
                       12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
                       16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
                       20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
                       70:"seventy", 80:"eighty", 90:"ninety", 1000:"one thousand"
                      }
    validate_integers(num)
    if num > 1000:
        raise ValueError("Sorry. The module only works for integers <= 1000.")
    if num < 1:
        raise ValueError("Sorry. The module only works for integers >= 1.")
    if num in numeral_to_word.keys():
        return numeral_to_word[num]

    if num < 100:
        tens = (num//10) * 10
        ones = num % 10
        return numeral_to_word[tens] + '-' + numeral_to_word[ones]

    hundreds = numeral_to_word[num//100] +' ' + 'hundred'
    if num % 100 == 0:
        return hundreds

    two_digits = number_to_word(num % 100)
    return hundreds + ' and ' + two_digits

def greatest_common_divisor(num_a, num_b):
    """Return greatest common divisor of num_a
    and num_b through Euclidian algorithim.
    """
    validate_integers(num_a, num_b)
    if num_b > num_a:
        num_a, num_b = num_b, num_a
    while num_b != 0:
        num_a, num_b = num_b, num_a % num_b
    return num_a

def lowest_common_multiple(num_a, num_b):
    """Return lowest common multiple. It is the product of num_a
    and num_b divided by the greatest common divisor.
    """
    validate_integers(num_a, num_b)
    gcd_result = greatest_common_divisor(num_a, num_b)
    result = (num_a * num_b) / gcd_result
    return int(result)

def load_text_file(filename):
    """ Returns a list of sequences separated by carriage returns in the file.
    Words are strings of characters. Whitespace is stripped. Capital letters removed.
    """
    in_file = open(filename, 'r')
    wordlist = []
    for line in in_file:
        wordlist.append(line.strip().lower())
    return wordlist

def horiz_value(coord_x, coord_y, grid):
    """Return the product of 4 adjacent cells in a dictionary."""
    try:
        product = (grid[(coord_x, coord_y)] * grid[(coord_x + 1, coord_y)] *
                   grid[(coord_x + 2, coord_y)] * grid[(coord_x + 3, coord_y)])
    except KeyError:
        return 0

    return product

def vertical_value(coord_x, coord_y, grid):
    """Return the product of 4 vertically adjacent cells in a dictionary."""
    try:
        product = (grid[(coord_x, coord_y)] * grid[(coord_x, coord_y + 1)] *
                   grid[(coord_x, coord_y + 2)] * grid[(coord_x, coord_y + 3)])
    except KeyError:
        return 0

    return product

def right_diagonal_value(coord_x, coord_y, grid):
    """Return the product of 4 right diagonally adjacent cells in a dictionary."""
    try:
        product = (grid[(coord_x, coord_y)] * grid[(coord_x + 1, coord_y + 1)] *
                   grid[(coord_x + 2, coord_y + 2)] * grid[(coord_x + 3, coord_y + 3)])
    except KeyError:
        return 0

    return product

def left_diagonal_value(coord_x, coord_y, grid):
    """Return the product of 4 left diagonally adjacent cells in a dictionary."""
    try:
        product = (grid[(coord_x, coord_y)] * grid[(coord_x - 1, coord_y + 1)] *
                   grid[(coord_x - 2, coord_y + 2)] * grid[(coord_x - 3, coord_y + 3)])
    except KeyError:
        return 0

    return product

def create_nine_digit_product(num):
    """ Create a nine digit string resulting from the concatenation of
    the product from num and  multipliers (1, 2, 3,).... Return 0 if string
    cannot be length 9.

    """
    result = ''
    counter = 1
    while len(result) < 9:
        result += str(num * counter)
        counter += 1
    if len(result) > 9:
        result = 0
    return result

def find_sum_of_digit_factorial(number):
    """Return the sum of the factorial value of the digits of a number."""
    factorials = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120,
                  6:720, 7:5040, 8:40320, 9:362880}
    number = str(number)
    result = 0
    for char in number:
        result += factorials[int(char)]
    return result

def sum_fifth_power_of_digits(number):
    """Return the sum of the fifth power of each digit of number."""
    fifth_powers = {0:0, 1: 1, 2: 32, 3: 243, 4: 1024, 5: 3125, 6: 7776,
                    7: 16807, 8: 32768, 9: 59049}
    result = 0
    for char in str(number):
        result += fifth_powers[int(char)]
    return result

def create_triangle_numbers(limit):
    """Return set of triangle numbers below limit."""
    triangles = {0}
    increment = 1
    value = 0
    while True:
        value += increment
        increment += 1
        if value > limit:
            break
        triangles.add(value)
    return triangles

def create_pentagon_numbers(limit):
    """Return a set of pentagon numbers up to limit."""
    pentagons = {0}
    increment = 1
    value = 0
    while True:
        value += increment
        increment += 3
        if value > limit:
            break
        pentagons.add(value)
    return pentagons

def create_hexagon_numbers(limit):
    """Return a set of hexagon numbers up to limit."""
    hexagons = {0}
    increment = 1
    value = 0
    while True:
        value += increment
        increment += 4
        if value > limit:
            break
        hexagons.add(value)
    return hexagons

def add_digits(number):
    """Return the sum of digits in a numeral."""
    validate_integers(number)
    result = 0
    number = str(number)
    for char in number:
        result += int(char)
    return result

def create_right_truncations(number):
    """Return a set of right truncations of a number: 123 -> {123, 12, 1}"""
    validate_integers(number)
    result = {number}
    number = str(number)
    while True:
        number = number[:-1:]
        if number == '':
            break
        result.add(int(number))
    return result

def create_left_truncations(number):
    """Return a set of left truncations of a number: 123 -> {123, 23, 3}"""
    validate_integers(number)
    result = {number}
    number = str(number)
    while True:
        number = number[1::]
        if number == '':
            break
        result.add(int(number))
    return result

def get_permutations(input_string):
    """Return all permutations of a given string."""
    perms = []
    if len(input_string) < 2:
        perms.append(input_string)
        return perms

    last_char = input_string[-1]
    input_string = input_string[0:-1]
    working_list = get_permutations(input_string)

    for sequence in working_list:
        counter_1 = 0
        while counter_1 < len(sequence):
            new_permutation = sequence[:counter_1] + last_char + sequence[counter_1:]
            perms.append(new_permutation)
            counter_1 += 1
        new_permutation = sequence + last_char
        perms.append(new_permutation)
    return perms

def word_score(word):
    """Return an integer corresponding to the sum of the
        ordinal value of each letter in a word.
    """
    result = 0
    for char in word:
        result = result + LOWERCASE_ALPHABET.index(char) +1
    return result

def find_goldbach_numbers(limit):
    """Return set of Goldbach numbers to limit. Goldbach proposed each odd
    composite is the sum of a square doubled and a prime number. Function
    returns numbers meeting second definition, including primes and even numbers.
    """
    goldbach_numbers = set()
    primes = prime_sieve(limit)
    doubled_squares = {i**2 * 2 for i in range(1, int(limit**.5))}
    for prime in primes:
        for doubled_square in doubled_squares:
            goldbach_number = doubled_square + prime
            if goldbach_number < limit:
                goldbach_numbers.add(goldbach_number)
    return goldbach_numbers

def equal_division(input_string, length_of_division):
    """ Divide a string up into a list of strings, each string as long
        as the specified length of division. Discard remainder.
    """
    divisions = []
    if len(input_string) < 2:
        raise ValueError('A single character cannot be divided')
    while input_string:
        new_division = input_string[0:length_of_division]
        if len(new_division) == length_of_division:
            divisions.append(new_division)
        input_string = input_string[length_of_division:]
    return divisions

def check_for_pattern(input_string):
    """ Check a string for a recurring pattern. If no pattern,
        return False. If pattern present, return smallest integer
        length of pattern.
        Warning: equal_divisions discards the remainder, so if it doesn't
        fit the pattern, you will get a false postive.
        The specific use is to check recurring decimal patterns, so it doesn't matter
        for that use.
    """
    if len(input_string) < 2:
        return False

    length_of_division = 1
    limit = len(input_string)//2

    while length_of_division < limit + 1:
        divisions = equal_division(input_string, length_of_division)
        divisions = set(divisions)
        if len(divisions) == 1:
            return length_of_division

        else:
            length_of_division += 1
    return False

def check_equations_for_primes(var_a, var_b, primes):
    """Return the number of consecutive primes that result for variable a and b for the formula:
        n**2 + an + b. Starting with zero"""
    counter = 0
    for i in range(0, 1000):
        temp = (i**2) + (i * var_a) + var_b
        if temp not in primes:
            break
        counter += 1
    return counter

def get_rotations(num):
    """Return set of rotations of a number. Output is an integer.
    123 --> 312, 231, 123.
    """
    validate_integers(num)
    num = str(num)
    rotations = set()
    rotations.add(int(num))
    if len(num) == 1:
        return rotations

    for i in range(1, len(num)):
        new_rotation = num[i:] + num[:i]
        rotations.add(int(new_rotation))
    return rotations

def is_palindrome(num):
    """Return True if num is palindromic."""
    num = str(num)
    if num == '':
        return False

    return num == num[::-1]

def is_binary_palindrome(num):
    """Return True if num is binary palindromic."""
    num = bin(num)
    num = num[2:]
    return num == num[::-1]

def create_fraction_list():
    """ Create a list of numerators and denominators. x/y < 0.
    No zeros.
    """
    output = []
    for numerator in range(10, 101):
        for denominator in range(10, 101):
            temp = set(str(numerator) +str(denominator))
            if len(temp) == 4:
                continue
            if '0' in temp:
                continue
            if numerator < denominator:
                output.append((numerator, denominator))
    return output

def apply_false_cancel(numerator, denominator):
    """Cancel the matching numeral in (numerator, denominator )"""
    numerator = str(numerator)
    denominator = str(denominator)
    for char_1 in numerator:
        for char_2 in denominator:
            if numerator == denominator:
                numerator.remove(char_1)
                denominator.remove(char_2)
                return


pytest.main(['-v'])
