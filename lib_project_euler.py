"""Library of functions used by Project Euler solutions."""

import math

def validate_integers(*nums):
    """Throws type error if any of the arguments are not integers."""
    for num in nums:
        if not isinstance(num, int):
            raise TypeError("Sorry. The function only works with integers.")

def fibonacci(index, cache=None):
    """ Return the Fibbonacci number of n index. Cache results."""
    validate_integers(index)
    if cache is None:
        cache = {1:1, 2:1, 3:2,}
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

    while potential_factors != set():
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

def find_prime_factors(num):
    """Find prime factors of num."""
    validate_integers(num)
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
    """Find the product of a string of digit characters, i.e, '23' produces 6"""
    num = list(num)
    product = 1
    for digit in num:
        product = product * int(digit)
    return product

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

def is_pyth_triplet(side_a, side_b, hypotenuse_c):
    """Return True if a, b, c compose a Pythagorean triplet."""
    validate_integers(side_a, side_b, hypotenuse_c)
    return (side_a**2) + (side_b**2) == (hypotenuse_c**2)

def find_factors(num):
    """Find factors of num, i.e. 6 returns {1, 2, 3, 6}"""
    validate_integers(num)
    factors = set()
    for i in range(1, int(num**.5)+ 1):
        if num % i == 0:
            factors.add(i)
            factors.add(int(num/i))
    return factors

def add_up_divisors(num):
    """Return sum of proper divisors of num, i.e. 6 returns 1+2+3."""
    validate_integers(num)
    divisors = find_factors(num)
    divisors.remove(num)
    return sum(divisors)

def find_collatz_stopping_time(num):
    """Find the length of the Collatz chain for num.
    12 would return 10 (inclusive of 1).
    """
    validate_integers(num)
    count = 1
    while num != 1:
        if num%2 == 0:
            num = num//2
            count += 1
        else:
            num = num*3 + 1
            count += 1
    return count

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
    validate_integers(num)
    comparison = '123456789'
    num = str(num)
    if len(num) > len(set(num)):
        return False

    num = set(num)
    comparison = set(comparison[0:len(num):1])
    return num == comparison


def find_combinations(number, r_items):
    """To find the number of combinations for n(number of things you are
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
    """Translate a counting number 1 to 1000.
    UK English string (uses 'and'), i.e. 1 -> 'one'.
    Internal whitespace and hypens are present. 152-> one hundred and fifty-two.
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
