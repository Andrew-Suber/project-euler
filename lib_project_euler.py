"""Library of functions and constants used by Project Euler solutions."""


import math
import string
import collections
from random import choice
import pytest


GOLDEN_RATIO = (1 + 5**.5)/2
GOLDEN_RATIO_CONJUGATE = (1 - 5**.5)/2
LOWERCASE_ALPHABET = string.ascii_lowercase


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """Represent the French deck of cards."""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def random_card(self, num):
        """Return a random card."""
        output = [choice(self) for _ in range(num)]
        return output

    def poker_hand(self):
        """Return a five card random hand."""
        return FrenchDeck.random_card(self, 5)


class IterationLimit():
    """Iteration limit that raises in response to
    value of the longest finite thread, pe_55."""

    def __init__(self, value=51):
        """First value is 51."""
        self.value = value

    def set_value(self, num):
        """Set value."""
        if num > self.value:
            print('limit', self.value, 'changes to', num)
            self.value = num

    def get_value(self):
        """Get value."""
        return self.value


def spades_high(card):
    """Return numeric value for each card in FrenchDeck."""
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


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
        cache = {0: 0, 1: 1, 2: 1, 3: 2}
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
    """Return the product of a string of digit characters,
    i.e, '23' produces 6.
    """
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
    for potential_factor in range(1, int(num**.5) + 1):
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
    """Translate a counting number 1 to 1,000 to
    UK English string (uses 'and'), i.e. 1 -> 'one'.
    Internal whitespace and hyphens are present.
    152-> one hundred and fifty-two.
    """

    numeral_to_word = {0: "", 1: "one", 2: "two", 3: "three", 4: "four",
                       5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                       10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                       14: "fourteen", 15: "fifteen", 16: "sixteen",
                       17: "seventeen", 18: "eighteen", 19: "nineteen",
                       20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
                       60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
                       1_000: "one thousand"}
    validate_integers(num)
    if num > 1_000:
        raise ValueError("Sorry. The module only works for integers <= 1,000.")
    if num < 1:
        raise ValueError("Sorry. The module only works for integers >= 1.")
    if num in numeral_to_word.keys():
        return numeral_to_word[num]

    if num < 100:
        tens = (num//10) * 10
        ones = num % 10
        return numeral_to_word[tens] + '-' + numeral_to_word[ones]

    hundreds = numeral_to_word[num//100] + ' ' + 'hundred'
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
    Words are strings of characters. Whitespace is stripped.
    Capital letters removed.
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
    """Return the product of 4 right diagonally
    adjacent cells in a dictionary.
    """
    try:
        product = (grid[(coord_x, coord_y)] *
                   grid[(coord_x + 1, coord_y + 1)] *
                   grid[(coord_x + 2, coord_y + 2)] *
                   grid[(coord_x + 3, coord_y + 3)])
    except KeyError:
        return 0

    return product


def left_diagonal_value(coord_x, coord_y, grid):
    """Return the product of 4 left diagonally
    adjacent cells in a dictionary.
    """
    try:
        product = (grid[(coord_x, coord_y)] *
                   grid[(coord_x - 1, coord_y + 1)] *
                   grid[(coord_x - 2, coord_y + 2)] *
                   grid[(coord_x - 3, coord_y + 3)])
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
    factorials = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120,
                  6: 720, 7: 5040, 8: 40320, 9: 362880}
    number = str(number)
    result = 0
    for char in number:
        result += factorials[int(char)]
    return result


def sum_fifth_power_of_digits(number):
    """Return the sum of the fifth power of each digit of number."""
    fifth_powers = {0: 0, 1: 1, 2: 32, 3: 243, 4: 1024, 5: 3125, 6: 7776,
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
            new_permutation = (sequence[:counter_1] +
                               last_char + sequence[counter_1:])
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
        result = result + LOWERCASE_ALPHABET.index(char) + 1
    return result


def find_goldbach_numbers(limit):
    """Return set of Goldbach numbers to limit. Goldbach proposed each odd
    composite is the sum of a square doubled and a prime number. Function
    returns numbers meeting second definition, including primes
    and even numbers.
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
        The specific use is to check recurring decimal patterns, so it doesn't
        matter for that use.
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
    """Return the number of consecutive primes that result for variable
    a and b for the formula: n**2 + an + b. Starting with zero.
    """
    counter = 0
    for i in range(0, 1_000):
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
    No zeros. No 11, 22, 33, etc. In ref to PE 33
    """
    fractions = []
    for numerator in range(10, 101):
        for denominator in range(10, 101):
            temp = set(str(numerator) + str(denominator))
            if len(temp) == 4:
                continue
            if '0' in temp:
                continue
            if (numerator % 11) == 0:
                continue
            if (denominator % 11) == 0:
                continue
            if numerator < denominator:
                fractions.append((numerator, denominator))
    return fractions


def apply_false_cancel(numerator, denominator):
    """Cancel the matching numeral in two two digit numbers and
    return the result or return 1 if not possible.
    """
    numerator = list(str(numerator))
    denominator = list(str(denominator))

    for char_1 in numerator:
        for char_2 in denominator:
            if char_1 == char_2:
                numerator.remove(char_1)
                denominator.remove(char_2)
                return(int(numerator[0]), int(denominator[0]))

    return (1, 1)


def is_substring_divisible(num):
    """Return True if a 10 digit numeral has substrings divisible by sequential
    prime numbers.
    """
    num = str(num)
    divisibility_condition = (int(num[1:4]) % 2 == 0 and
                              int(num[2:5]) % 3 == 0 and
                              int(num[3:6]) % 5 == 0 and
                              int(num[4:7]) % 7 == 0 and
                              int(num[5:8]) % 11 == 0 and
                              int(num[6:9]) % 13 == 0 and
                              int(num[7:10]) % 17 == 0)
    return divisibility_condition


def is_sequence(nums):
    """Return True if a set of numbers is sequential i.e. 8, 11, 14, 17."""
    nums = sorted(list(nums))
    if len(nums) < 3:
        return False

    while nums:
        first_difference = nums[1] - nums[0]
        second_difference = nums[2] - nums[1]
        if first_difference != second_difference:
            return False

        if len(nums) < 4:
            break
        nums.pop(0)
    return True


def get_armstrong_value(num):
    """Return Armstrong value of a number, this is the sum of n**k
    for each digit, where k is the length of the numeral.
    I.e 54 -> 5**2 + 4**2 -> 41.
    Related to narcisstic numbers and pluperfect digital invariants.
    """
    num = str(num)
    length = len(num)
    armstrong_value = 0
    for char in num:
        armstrong_value += int(char)**length
    return armstrong_value


def is_armstrong(num):
    "Return True if number is Armstrong number."""
    return num == get_armstrong_value(num)


def is_permutation(inputs):
    """Return True if strings in list are permutations of each other."""
    if len(inputs) < 2:
        return False

    identity_of_inputs = set()
    for item in inputs:
        item = str(item)
        if len(item) < 2:
            return False

        item = sorted(list(item))
        identity_of_inputs.add(str(item))
    return len(identity_of_inputs) == 1


def find_digit_sum(num):
    """Return the sum of digits in num."""
    num = str(num)
    digit_sum = 0
    for char in num:
        digit_sum += int(char)
    return digit_sum


def find_last_digits_power(base, exponent, digit_length):
    """Return the last digits of a very large power."""
    counter = 1
    result = base
    while counter < exponent:
        result = result * base
        result = str(result)[0:digit_length]
        result = int(result)
        counter += 1
    return result


def encrypt_with_xor(message, key):
    """Encrypt message using xor cipher with key. The ascii code for each
    character of message is returned after the xor function is applied to each
    bit of the character with the ascii code of the cycling key.
    The algorithim is symmetric, the same process with the same key will both
    encrypt and decrypt.
    """
    from itertools import cycle

    coded_message = ''
    for (message_char, key_char) in zip(message, cycle(key)):
        coded_char = chr(ord(message_char) ^ ord(key_char))
        coded_message += coded_char
    return coded_message


def is_in_wordlist(word):
    """Return True if word is in Linux wordlist at
    /usr/share/dict/american-english.
    """
    wordlist = load_text_file('/usr/share/dict/american-english')
    wordlist = set(wordlist)
    return word in wordlist


def text_to_ascii(text):
    """Return list of integers corresponding to the ascii codes of
    the characters of the text.
    """
    output = []
    for char in text:
        output.append(ord(char))
    return output


def ascii_to_text(list_of_ascii_codes):
    """Return string corresponding to the list of ascii codes input."""
    output = ''
    for num in list_of_ascii_codes:
        output += chr(num)
    return output


def generate_key_guesses():
    """Return list of every possible three undercase letter combination."""
    output = []
    for char_1 in LOWERCASE_ALPHABET:
        for char_2 in LOWERCASE_ALPHABET:
            for char_3 in LOWERCASE_ALPHABET:
                output.append(char_1 + char_2 + char_3)
    return output

def reverse_int(num):
    """Return the integer that is the reverse of num."""
    return int(str(num)[::-1])


def reverse_and_add(num):
    """Add num to its reverse. Basic step in 196-algorithim."""
    next_step = num + reverse_int(num)
    return next_step


def find_thread_length(num):
    """Return length of thread of num."""
    thread_length = 1
    temp = num

    while thread_length < iteration_limit_a.get_value():
        temp = reverse_and_add(temp)

        if is_palindrome(temp):
            return thread_length

        thread_length += 1
    return thread_length

def find_lychrel_numbers(limit):
    """Find Lychrel numbers up to limit."""
    lychrel_numbers = []

    for num in range(1, limit):
            lychrel_numbers.append(counter)


    print(f'There were {len(lychrel_numbers)} Lychrel numbers from 1 to {limit}:')
    return lychrel_numbers


pytest.main(['-v'])
