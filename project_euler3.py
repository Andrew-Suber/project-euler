"""Refactoring, organization of completed Project Euler problems.
Each Project Euler problem uses a function named pe_foo.
To perform a computation, invoke a function from the command line, like so:
python3 -c 'import euler_project.py; print(project_euler3.pe_foo())'
Start date: 6/21/19.
These modules use Python 3.
"""

import datetime
import decimal
import lib_project_euler as lpe


def pe_1():
    """Return the sum of mod 5 and mod 3 integers under 1,000."""
    result = 0
    for i in range(1, 1_000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return f'The sum of mod 5 and mod 3 integers under 1,000 is {result:,}.'


def pe_2():
    """Return the sum of all even fibonacci numbers under 4,000,000."""
    counter = 1
    result = 0
    while lpe.fibonacci(counter) < 4_000_000:
        if lpe.fibonacci(counter) % 2 == 0:
            result += lpe.fibonacci(counter)
        counter += 1
    return ('The sum of all even fibonacci numbers'
            f' under 4,000,000 is {result:,}')


def pe_3():
    """Return the largest prime factor of the test number."""
    test_number = 600851475143
    result = max(lpe.find_prime_factors(test_number))
    return f'The largest prime factor of 600,851,475,143 is {result:,}'


def pe_4():
    """Return the largest palindromic product of two three- digit
    numbers.
    """
    solutions = set()
    for value_a in range(999, 100, -1):
        for value_b in range(999, 100, -1):
            product = value_a * value_b
            product_string = str(product)
            if product_string == product_string[::-1]:
                solutions.add((product))
    solution = max(solutions)
    return ('The largest palindromic product'
            f' of two three-digit numbers is {solution:,}.')


def pe_5():
    """Return the smallest number divisible by all factors from 1 to limit."""
    limit = 20
    potential_factors = lpe.prime_sieve(limit)
    factors = []
    product = 1
    for num in potential_factors:
        root = num
        while True:
            if (num * root) > limit:
                break
            num *= root
        factors.append(num)
    for num in factors:
        product *= num
    return ('The smallest number divisible by all'
            f' factors from 1 to 20 is {product:,}.')


def pe_6():
    """Return the difference between the sum of all squares of all
    numbers from 1 to 100 and the square of the sum of all numbers from 1 to
    100."""
    integers = [i for i in range(1, 101)]
    sum_of_squares = 0
    square_of_sum = (sum(integers))**2
    for i in integers:
        sum_of_squares += i**2
    answer = square_of_sum - sum_of_squares
    return f'The solution for project euler 6 is {answer:,}.'


def pe_7():
    """Return the 10,001st prime number."""
    primes = list(lpe.prime_sieve(2_000_00))
    primes.sort()
    return f'The 10,001st prime number is {primes[10_000]:,}.'


def pe_8():
    """Return largest product from multiplication of 13 adjacent
    digits in file."""
    with open('files/pe_8_sample.txt') as pe_8_sample:
        sample = pe_8_sample.read()
    best_result = 0
    index = 0
    while index < len(sample) - 12:
        current_product = lpe.find_product(sample[index:index + 13])
        if current_product > best_result:
            best_result = current_product
        index += 1
    return f'{best_result:,} is the answer to project euler problem 8.'


def pe_9():
    """Return pythagorean triplet that sums to 1,000."""
    limit = 1_000
    for hypotenuse_c in range(334, limit//2):
        for side_a in range(1, (limit - hypotenuse_c)//2):
            b_side = (limit - hypotenuse_c) - side_a
            if lpe.is_pyth_triplet(side_a, b_side, hypotenuse_c):
                return ('The pythagorean triplet that sums to 1,000 is:'
                        f'{side_a, b_side, hypotenuse_c}')

    return 'No triplet was found for sum limit {limit}.'


def pe_10():
    """Return the sum of all primes below 2,000,000."""
    primes = set(lpe.prime_sieve(2_000_000))
    result = sum(primes)
    return f'The sum of all primes below 2,000,000 is {result:,}.'


def pe_11():
    """Return largest product in adjacent cells of a grid."""
    current_file = 'files/pe_11_grid.txt'
    grid = lpe.load_text_file(current_file)
    point_x, point_y = 0, 0
    grid_2 = {}
    while grid:
        current_line = grid.pop(0)
        current_line = current_line.split(' ')
        point_x = 0
        while current_line:
            current_value = current_line.pop(0)
            current_value = int(current_value)
            grid_2[(point_x, point_y)] = current_value
            point_x += 1
        point_y += 1
    high_value = 0
    for key in grid_2:
        point_x, point_y = key[0], key[1]
        value = lpe.horiz_value(point_x, point_y, grid_2)
        high_value = max(value, high_value)
        value = lpe.vertical_value(point_x, point_y, grid_2)
        high_value = max(value, high_value)
        value = lpe.left_diagonal_value(point_x, point_y, grid_2)
        high_value = max(value, high_value)
        value = lpe.right_diagonal_value(point_x, point_y, grid_2)
        high_value = max(value, high_value)
    return f'The highest product in the given grid is {high_value:,}'


def pe_12():
    """Return first triangle number with over 500 divisors."""
    counter = 2
    triangle = 1
    while True:
        triangle = triangle + counter
        factors = len(lpe.find_factors(triangle))
        if factors > 500:
            break
        counter = counter + 1
    return f'The first triangle number with over 500 divisors is {triangle:,}'


def pe_13():
    """Read file consisting of large numbers. Sum numbers. Return
    first ten digits of sum.
    """
    with open('files/pe_13_sample.txt') as pe_13_sample:
        sample = pe_13_sample.read()
    lines = sample.split()
    total = 0
    for line in lines:
        total += int(line)
    result = str(total)[0:10]
    return f'{result} is the answer to project euler problem 13.'


def pe_14():
    """Return the number with the largest collatz stopping time."""
    limit = 500_000
    best_result = (0, 0)
    for integer in range(1, limit):
        length = lpe.find_collatz_stopping_time(integer)
        if best_result[1] < length:
            best_result = (integer, length)
    result = (f'{best_result[0]:,} is the number with the highest Collatz '
              f'stopping time under {limit}: {best_result[1]} iterations.')
    return result


def pe_15():
    """Return the number of possible distinct paths
    in a square lattice 20x20.
    """
    result = lpe.find_combinations(40, 20)
    return f'The number of possible paths in a lattice 20x20 is {result:,}.'


def pe_16():
    """Give the sum of the digits of 2**1,000."""
    num = str(2**1_000)
    total = 0
    for char in num:
        total += int(char)
    return f'The sum of the digits of 2 to the thousandth power is {total:,}.'


def pe_17():
    """Sum the number of characters in the UK words representing the
    integers from 1 to 1,000. Exclude dashes and spaces.
    """
    total = 0
    for number_word in range(1, 1001):
        number_word = lpe.number_to_word(number_word)
        number_word = number_word.replace('-', '')
        number_word = number_word.replace(' ', '')
        total += len(number_word)
    return ('The sum of characters in the number'
            f' words from 1 to 1,000 is {total:,}.')


def pe_18():
    """solve pe 18. """
    pass


def pe_19():
    """Return how many times the first of the month was also a Sunday for the
    20th century."""
    number_of_sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime.datetime(year, month, 1).weekday() == 6:
                number_of_sundays += 1
    return (f'{number_of_sundays:,} Sundays'
            ' fell on the 1st in the 20th century.')


def pe_20():
    """Return the sum of all the digits in 100 factorial."""
    product = 1
    for integer in range(1, 101):
        product = product * integer
    result = lpe.add_digits(product)
    return f'The sum of all the digits in 100 factorial is {result:,}.'


def pe_21():
    """Return the sum of all amicable number pairs up to 10,000."""
    amicable_pairs = set()
    for number in range(2, 10_000):
        if lpe.is_amicable(number):
            amicable_pairs.add(number)
            amicable_pairs.add(lpe.add_up_divisors(number))
    result = sum(amicable_pairs)
    return f'The sum of amicable pairs under 10,000 is {result:,}.'


def pe_22():
    """Give a word score for each word in a list. The word score is the sum of
    the index of the letters multiplied by the number in the list.
    """
    new_names = []
    result = 0
    names = lpe.load_text_file('files/pe_22_name_list.txt')
    names = names[0]
    names = names.split(",")
    for word in names:
        new_word = word.replace('"', '')
        # Replace double quote with no character
        new_names.append(new_word)
    new_names = sorted(new_names)
    for word in new_names:
        product = lpe.word_score(word) * (new_names.index(word) + 1)
        result += product
        print(word, 'product:', product, 'result:', result)
    return f'The sum of word scores is {result:,}.'


def pe_23():
    """Return the sum of all numbers that
    are not the sum of two abundant numbers
     at the mathematically proven limit 28,123.
    """
    abundant_numbers_a = []
    abundant_sums = set()
    limit = 28123
    for number in range(1, limit + 1):
        if lpe.is_abundant(number):
            abundant_numbers_a.append(number)
    abundant_numbers_b = abundant_numbers_a[:]
    for num_a in abundant_numbers_a:
        for num_b in abundant_numbers_b:
            abundant_sum = num_a + num_b
            if abundant_sum <= limit:
                abundant_sums.add(abundant_sum)
    integers = {number for number in range(1, limit + 1)}
    non_abundant_sums = integers.difference(abundant_sums)
    _ = sum(non_abundant_sums)
    return ('The sum of all numbers that are '
            f'not the sum of two abundant numbers is {_:,}.')


def pe_24():
    """Return the millionth lexicographically
    sorted permutation of 0123456789.
    """
    permutations = lpe.get_permutations("0123456789")
    permutations = sorted(permutations)
    result = permutations[999999]
    return f'The millionth sorted permutation of 0123456789 is {result}.'


def pe_25():
    """Return the index of the first Fibonacci number with 1,000 digits."""
    fib_index = 0
    current_fib = lpe.fibonacci(fib_index)
    while len(str(current_fib)) < 1_000:
        fib_index += 1
        current_fib = lpe.fibonacci(fib_index)
    return ('The index of the first Fibonacci '
            f'number with 1,000 digits is {fib_index}.')


def pe_26():
    """Return the 1/x fraction where x < 1,000 that leads to the fraction with
    the longest repeating recurring cycle in the decimal portion.
    """
    decimal.getcontext().prec = 5_000
    numerator = decimal.Decimal(1)
    best_result = 0
    for denominator in range(1, 1_001):
        denominator = decimal.Decimal(denominator)
        fraction = decimal.Decimal(numerator/denominator)
        pattern_length = lpe.check_for_pattern(str(fraction)[10:-5])
        if pattern_length > best_result:
            best_result = denominator
    return ('The denominator under 1,000 that produces the longest '
            f'recurring cycle in the decimal portion is {best_result}.')


def pe_27():
    """Return the values that generate the most
    consecutive prime numbers in the
    equation of the form n**2 + n*a + b where n is a range of values starting
    at 0. a and b can be subtracted as well as added.
    """
    best_result = 0
    primes = set(lpe.prime_sieve(2_001_000))
    # According to the problem statement, 1,000**2 + 1,000*1,000 + 1,000
    # is the largest number that could have to be checked.
    integers = {i for i in range(-1001, 1001)}
    potential_values_a = integers.copy()
    potential_values_a.discard(0)
    integers = set(filter(lambda x: abs(x) in primes, integers))
    # B must have a prime value. Otherwise when N is 0,
    # the result wouldn't be prime.
    potential_values_b = integers.copy()
    potential_values_b.discard(0)

    for term_a in potential_values_a:
        for term_b in potential_values_b:
            primes_count = lpe.check_equations_for_primes(term_a,
                                                          term_b, primes)
            if primes_count > best_result:
                best_result = primes_count
                result = term_a * term_b
                print('n**2 + na + b: a=', term_a, 'b=', term_b,
                      ': Number of consecutive primes produced:', primes_count)
    return f'The solution for PE 27 is {result}.'


def pe_28():
    """Return the sum of the diagonals of a spiral of integers. If you arrange
    the integers in a square, find the diagonals from the center. I.e the first
    layer would have 3,5,7,9 at the corners.
    """
    addition_increment = 2
    corner_numbers = [1]
    limit = 1001
    current_position = 1

    while addition_increment < limit:
        counter = 0
        while counter < 4:
            current_position += addition_increment
            corner_numbers.append(current_position)
            counter += 1
        addition_increment += 2
    result = sum(corner_numbers)
    return ('The sum of the diagonals in an '
            f'integer square 1001 * 1001 = {result:,}.')


def pe_29():
    """Return the number of distinct powers for the form a**b for 1 <= a <= 100
    and 1 <= b <= 100.
    """
    distinct_powers = set()
    for term_a in range(2, 101):
        for term_b in range(2, 101):
            result = term_a**term_b
            distinct_powers.add(result)
    return (f'There are {len(distinct_powers)} distinct powers for a**b '
            'where 2 <= a <= 100 and 2 <= b <= 100.')


def pe_30():
    """Return the sum of all numbers that are equal to the sum of
    the fifth power of their digits.
    """
    limit = 999999
    # It is impossible for this condition to be met below this limit because
    # 354294 < 999999
    result = 0
    for number in range(10, limit):
        if number == lpe.sum_fifth_power_of_digits(number):
            result += number
    return ('The sum of all numbers equal to the sum'
            f' of the fifth power of their digits is {result:,}.')


def pe_32():
    """Return multiplicand, multiplier and product strings that are
    pandigital e.g. 123456789.
    """
    pan_digit_products = set()
    for multiplicand in range(2, 2_000):
        for multiplier in range(2, 2_000):
            product = multiplicand * multiplier
            joined_string = str(multiplicand) + str(multiplier) + str(product)
            if len(str(joined_string)) == 9:
                if lpe.is_pan_digital(joined_string):
                    pan_digit_products.add(product)
    result = sum(pan_digit_products)
    return f'The sum of possible pandigital products is {result:,}.'


def pe_33():
    """Return all false cancelling fractions of form xx/yy."""
    limit = .001
    results_list = []
    fraction_list = lpe.create_fraction_list()

    for fraction in fraction_list:
        first_ratio = fraction[0]/fraction[1]
        result = lpe.apply_false_cancel(fraction[0], fraction[1])
        second_ratio = result[0]/result[1]
        if abs(first_ratio - second_ratio) < limit:  # Float math
            print('Bingo!', fraction, result, first_ratio, second_ratio)
            results_list.append(fraction)

    numerator_product = 1
    denominator_product = 1
    for (numerator, denominator) in results_list:
        numerator_product *= numerator
        denominator_product *= denominator
    gcd = lpe.greatest_common_divisor(numerator_product, denominator_product)
    result = int(denominator_product/gcd)
    return ''.join([f'{results_list} are the false cancelling fractions.',
                    f' {result} is the denominator of their product expressed',
                    ' in simplest terms.'])


def pe_34():
    """Return all numbers that are equal to the sum of the factorial of their
    digits.
    """
    limit = 2540160
    # It is impossible for for this sum to be equal for a number > 7 * 9!
    result = 0
    for number in range(10, limit):
        if number == int(lpe.find_sum_of_digit_factorial(number)):
            result += number
    return f'The solution for Project Euler 34 is {result:,}'


def pe_35():
    """Return circular primes under a million. These are primes where each
    rotation is a prime.
    """
    rotational_primes = set()
    primes = lpe.prime_sieve(1_000_000)
    for prime in primes:
        rotations = lpe.get_rotations(prime)
        if rotations.issubset(primes):
            rotational_primes.add(prime)
    return (f'There are {(len(rotational_primes))} '
            'rotational primes under 1,000,000.')


def pe_36():
    """Return the sum of all numbers under 1,000,000 that are palindromic in
    decimal and binary representation.
    """
    result = 0
    for num in range(1, 1_000_000):
        if lpe.is_palindrome(num):
            if lpe.is_binary_palindrome(num):
                result += num
    return ('The sum of n < 1,000,000 both palindromic '
            f'in decimal and binary is {result}.')


def pe_37():
    """Return all two-sided primes i.e. primes that are truncatable both left
    and right and result in primes at each truncation.
    """
    two_sided_primes = set()
    primes = lpe.prime_sieve(1_000_000)
    # The highest such prime is 739397. Adding any digit to it will not result
    # in another truncatable prime, ergo, it is the highest one possible.
    for prime in primes:
        if prime < 10:
            continue
        right_truncs = lpe.create_right_truncations(prime)
        left_truncs = lpe.create_left_truncations(prime)
        total_truncs = right_truncs.union(left_truncs)
        if total_truncs.issubset(primes):
            two_sided_primes.add(prime)
    result = sum(two_sided_primes)
    return f'The sum of all two-sided primes is {result:,}.'


def pe_38():
    """ Return pandigital products."""
    pandigital_products = set()
    for num in range(2, 9999):
        concatenated_product = lpe.create_nine_digit_product(num)
        if lpe.is_pan_digital(concatenated_product):
            pandigital_products.add(int(concatenated_product))
    result = max(pandigital_products)
    return f'The solution for Project Euler 38 is {result:,}.'


def pe_40():
    """Return the product of the 1, 10th, 100th, etc. digit of Champernowe's
    Constant.
    """
    digit_string = ''
    counter = 1
    limit = 1_000_000
    while counter <= limit:
        digit_string = digit_string + str(counter)
        counter += 1
    indices = [0, 9, 99, 999, 9_999, 99_999, 999_999]
    result = 1
    for index in indices:
        result *= int(digit_string[index])
    return f'The solution for Project Euler 40 is {result:,}.'


def pe_41():
    """Return the largest pandigital prime possible."""
    pan_digit_primes = set()
    primes = lpe.prime_sieve(10_000_000)
    for prime in primes:
        if lpe.is_pan_digital(prime):
            pan_digit_primes.add(prime)
    result = max(pan_digit_primes)
    return f'The largest possible pandigital prime is {result:,}.'


def pe_42():
    """Return each word with a word value equal to a triangle number in
    the relevant file.
    """
    current_file = 'files/pe_42_words.txt'
    word_list = lpe.load_text_file(current_file)
    word_list = word_list[0]
    word_list = word_list.replace('"', '')  # Remove double quote
    word_list = word_list.split(',')
    triangles = lpe.create_triangle_numbers(1_000)
    # Equivalent to a word with 38 Zs
    triangle_word_counter = 0
    for word in word_list:
        word_value = lpe.word_score(word)
        if word_value in triangles:
            triangle_word_counter += 1
            print(f'{word} has a triangle number for its word value.')
    return ('The number of triangle words in the'
            f' file is {triangle_word_counter}.')


def pe_43():
    """Find a pandigital numeral where successive substrings are divisible
    by successive primes.
    """
    result = 0
    pandigitals = lpe.get_permutations('0123456789')
    pandigitals = set(filter(lambda x: x[0] != '0', pandigitals))
    for pandigital in pandigitals:
        if lpe.is_substring_divisible(pandigital):
            print(pandigital)
            result += int(pandigital)
    return f'{result:,}'


def pe_44():
    """Return two pentagonal numbers that have a difference and sum equal to
    another pentagonal number, specifically, the pair with the smallest
    possible difference.
    """
    pentagons_a = lpe.create_pentagon_numbers(4_000)
    pentagons_b = pentagons_a.copy()
    for pent_a in pentagons_a:
        for pent_b in pentagons_b:
            difference = abs(pent_a - pent_b)
            total = pent_a + pent_b
            if difference in pentagons_a and total in pentagons_a:
                result = difference
    return f'The result for Project Euler problem 44 is {result}.'


def pe_45():
    """Return the second triangle number that is also a pentagon number and a
    hexagon number.
    """
    limit = 1_600_000_000
    triangles = lpe.create_triangle_numbers(limit)
    pentagons = lpe.create_pentagon_numbers(limit)
    hexagons = lpe.create_hexagon_numbers(limit)
    results = set()
    for number in triangles:
        if number in pentagons and number in hexagons:
            results.add(number)
    return ('The numbers that are triagonal, hexagonal'
            f' and pentgonal below 2 billion are {results}.')


def pe_46():
    """ Goldbach proposed that each odd composite is a sum of a square times
    two and a prime.

    Return the first integer that disproves this proposal.
    """
    limit = 10_000
    # The limit was found by running the function with larger limits
    composites = lpe.find_composites(limit)
    odd_composites = set(filter(lambda x: x % 2 != 0, composites))
    goldbach_numbers = lpe.find_goldbach_numbers(limit)
    result = min(odd_composites.difference(goldbach_numbers))
    return ''.join(['The first odd composite that is not the sum of',
                    f' a doubled square and a prime is {result:,}.'])


def pe_48():
    """Return the last ten digits of the sum of the 'self powers', i.e. n ** n
    from 1 to 1,000.
    """
    result = 0
    limit = 1_000
    for number in range(1, limit + 1):
        result += number ** number
    result = str(result)[-10::]
    return f'The last ten digits of the sum of the self powers is {result}.'


def pe_49():
    """Return 4-digit prime that has 3 prime permutations in an
    arithmetic sequence.
    """
    primes = lpe.prime_sieve(10_000)
    four_digit_primes = set(filter(lambda x: len(str(x)) == 4, primes))
    prime_permutations = []
    for prime in four_digit_primes:
        prime_permutation = set(lpe.get_permutations(str(prime)))
        prime_permutation = [int(x) for x in prime_permutation
                             if int(x) in primes]
        prime_permutation.sort()
        prime_permutations.append(prime_permutation)
    for group in prime_permutations:
        while group:
            if lpe.is_sequence(group):
                return f'The sequence of permuted primes is {group}.'

            group.pop(0)


def pe_50():
    """Return the largest prime under a million that is composed of a sum of
    consecutive primes.
    """
    primes_1 = lpe.prime_sieve(1_000_000)
    line_segment_length = 550
    # Limit was found by running the script with incrementally larger limits
    best_result = 2

    while True:
        primes_2 = sorted(list(primes_1))
        while primes_2:
            line_segment = primes_2[:line_segment_length]
            total = sum(line_segment)
            if total in primes_1:
                if len(line_segment) > best_result:
                    return (f'{total:,} is the sum of the sequence of primes '
                            f'from {line_segment[0]} to {line_segment[-1]}, '
                            f'that sequence is {len(line_segment)}'
                            ' primes long.')

            primes_2.pop(0)
        line_segment_length -= 1


def pe_51():
    """Return the first x so that 2x, 3x, 4x, 5x and 6x are
    permutations of each other.
    """
    counter = 1
    while True:
        multiples = [counter*2, counter*3, counter*4, counter*5, counter*6]
        if lpe.is_permutation(multiples):
            return (f'{counter:,} is the first integer'
                    ' with multiples that are permutations.')

        counter += 1


def pe_53():
    """Find the number of possible permutation counts over 1,000,000 for
    n choose r where n <= 100.
    """
    item_number = 1
    permutation_count = 0
    while item_number < 101:
        for choice_number in range(1, item_number + 1):
            number_of_permutations = lpe.find_combinations(item_number,
                                                           choice_number)
            if number_of_permutations > 1_000_000:
                permutation_count += 1
        item_number += 1
    return (f'{permutation_count} is the number of '
            'permutation counts over 1,000,000'
            ' for n choose r where n <=100.')


def pe_55():
    """Find the number of Lychrel numbers under 10_000."""
    from ple import IterationLimit
    iteration_limit_a = IterationLimit()
    limit = 10_000


def pe_56():
    """Find the expression of a**b where a,b < 100
    with the maximal digit sum.
    """
    best_result = 0
    for base in range(1, 100):
        for exponent in range(1, 100):
            result = base**exponent
            digit_sum = lpe.find_digit_sum(result)
            if digit_sum > best_result:
                best_result = digit_sum
    return f'{best_result} is the largest digit sum for a**b where a,b < 100.'


def pe_59():
    """Decrypt an XOR encrypted message. Key is three random lowercase letters.
    Check against wordlist.
    """
    wordlist = lpe.load_text_file('/usr/share/dict/american-english')
    wordlist = set(wordlist)
    current_file = 'files/p059_cipher.txt'
    coded_message = lpe.load_text_file(current_file)
    coded_message = coded_message[0]
    coded_message = coded_message.split(',')
    coded_message = [chr(int(char)) for char in coded_message]
    key_guesses = lpe.generate_key_guesses()
    best_result = 1
    best_decryption = ''
    for guess in key_guesses:
        word_count = 0
        unencrypted = lpe.encrypt_with_xor(coded_message, guess)
        words = unencrypted.split()
        for word in words:
            if word in wordlist:
                word_count += 1
        if word_count > best_result:
            best_result = word_count
            best_decryption = unencrypted
            print('key =', guess, '\n', best_decryption,
                  'viable words =', word_count, '\n')
    ascii_sum = 0
    for char in best_decryption:
        ascii_sum += ord(char)
    return ('The sum of the ascii codes of the'
            f' properly decrypted message is {ascii_sum:,}.')


def pe_63():
    """Find the number of powers that have as many digits as the value of the
    exponent. I.e 7**5 is a five digit number.
    """
    digit_power_count = 0
    for base in range(1, 100):
        for exponent in range(1, 100):
            result = base**exponent
            if len(str(result)) == exponent:
                digit_power_count += 1
    return (f'{digit_power_count} are the number of powers'
            ' that have a length equal to the exponent.')


def pe_92():
    """Return all the 'sad' numbers under 10,000,000."""
    limit = 10_000_000
    happy_count = 0

    for integer in range(1, limit + 1):
        if lpe.is_happy(integer):
            happy_count += 1
    sad_count = limit - happy_count
    return f'There are {sad_count:,} numbers from 1 to {limit:,} that are sad.'


def pe_97():
    """Find the last digits of a very large non-Mersenne prime."""
    base = 2
    for _ in range(7_830_456):
        base = (base * 2) % 10_000_000_000
    result = base * 28_433 + 1
    result = str(result)[-10:]
    return f'The last ten digits of the very large prime are {result}.'
