
"""Refactoring, organization of completed Project Euler problems.
Each Project Euler problem uses a function named pe_foo.
To perform a computation, invoke a function from the command line, like so:
python -c 'import euler_project.py; print(project_euler3.pe_foo())'
Start date: 6/21/19.
"""


import pytest
import lib_project_euler as lpe


def pe_1():
    """ Return the sum of mod 5 and mod 3 integers under 1000."""
    result = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return f'The sum of mod 5 and mod 3 integers under 1000 is {result}.'

def pe_2():
    """ Return the sum of all even fibonacci numbers under 4,000,000."""
    counter = 1
    result = 0
    while lpe.fibonacci(counter) < 4000000:
        if lpe.fibonacci(counter) % 2 == 0:
            result += lpe.fibonacci(counter)
        counter += 1
    return f'The sum of all even fibonacci numbers under 4,000,000 is {result}'

def pe_3():
    """ Find the largest prime factor of the test number."""
    test_number = 600851475143
    result = max(lpe.find_prime_factors(test_number))
    return f'The largest prime factor of 600851475143 is {result}'

def pe_4():
    """Find the largest palindromic product of two three- digit
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
    return f'The largest palindromic product of two three-digit numbers is {solution}.'

def pe_5():
    """Find the smallest number divisible by all factors from 1 to limit."""
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
    return f'The smallest number divisible by all factors from 1 to 20 is {product}.'

def pe_6():
    """Find the difference between the sum of all squares of all
    numbers from 1 to 100 and the square of the sum of all numbers from 1 to
    100."""
    integers = [i for i in range(1, 101)]
    sum_of_squares = 0
    square_of_sum = (sum(integers))**2
    for i in integers:
        sum_of_squares += i**2
    answer = square_of_sum - sum_of_squares
    return f'The solution for project euler 6 is {answer}.'

def pe_7():
    """Find the 10,001st prime number."""
    primes = list(lpe.prime_sieve(200000))
    primes.sort()
    return f'The 10,001st prime number is {primes[10000]}.'

def pe_8():
    """Find largest product from multiplication of 13 adjacent
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
    return f'{best_result} is the answer to project euler problem 8.'

def pe_9():
    """Find pythagorean triplet that sums to 1000."""
    limit = 1000
    for hypotenuse_c in range(334, limit//2):
        for side_a in range(1, (limit - hypotenuse_c)//2):
            b_side = (limit -  hypotenuse_c) - side_a
            if lpe.is_pyth_triplet(side_a, b_side, hypotenuse_c):
                return ''.join(['The pythagorean triplet that sums to 1000 is:',
                                f'{side_a, b_side, hypotenuse_c}'])
    return 'No triplet was found for sum limit {limit}.'

def pe_10():
    """Find the sum of all primes below 2,000,000."""
    primes = set(lpe.prime_sieve(2000000))
    result = sum(primes)
    return f'The sum of all primes below 2,000,000 is {result}.'

def pe_11():
    """Find largest product in adjacent cells of a grid."""
    grid = lpe.load_text_file('files/pe_11_grid.txt')
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
    return f'The highest product in the given grid is {high_value}'

def pe_12():
    """Find first triangle number with over 500 divisors."""
    counter = 0
    triangle = 0
    while True:
        triangle = triangle + counter
        factors = len(lpe.find_factors(triangle))
        if factors > 500:
            break
        counter = counter + 1
    return f'The first triangle number with over 500 divisors is {triangle}'

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
    """Find the number with the largest collatz stopping time."""
    limit = 500000
    best_result = (0, 0)
    for integer in range(1, limit):
        length = lpe.find_collatz_stopping_time(integer)
        if best_result[1] < length:
            best_result = (integer, length)
    result = ''.join((f'{best_result[0]} is the number with the highest Collatz ',
                      f'stopping time under {limit}: {best_result[1]} iterations.'))
    return result

def pe_15():
    """Find the number of possible distinct paths in a square lattice 20x20."""
    result = lpe.find_combinations(40, 20)
    return f'The number of possible paths in a lattice 20x20 is {result}.'

def pe_16():
    """Give the sum of the digits of 2**1000."""
    num = str(2**1000)
    total = 0
    for char in num:
        total += int(char)
    return f'The sum of the digits of 2 to the thousandth power is {total}.'

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
    return f'The sum of characters in the number words from 1 to 1,000 is {total}.'

def pe_18():
    """solve pe 18. """
    pass

def pe_20():
    """Find the sum of all the digits in 100 factorial."""
    product = 1
    for integer in range(1, 101):
        product = product * integer
    result = lpe.add_digits(product)
    return f'The sum of all the digits in 100 factorial is {result}.'

def pe_21():
    """Find the sum of all amicable number pairs up to 10,000."""
    amicable_pairs = set()
    for number in range(2, 10000):
        if lpe.is_amicable(number):
            amicable_pairs.add(number)
            amicable_pairs.add(lpe.add_up_divisors(number))
    result = sum(amicable_pairs)
    return f'The sum of amicable pairs under 10,000 is {result}.'

def pe_23():
    """Find the sum of all numbers that are not the sum of two abundant numbers
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
    result = sum(non_abundant_sums)
    return f'The sum of all numbers that are not the sum of two abundant numbers is {result}.'

def pe_24():
    """Find the millionth lexicographically sorted permutation of 0123456789"""
    permutations = lpe.get_permutations("0123456789")
    permutations = sorted(permutations)
    result = permutations[999999]
    return f'The millionth sorted permutation of 0123456789 is {result}.'

def pe_30():
    """Find the sum of all numbers that are equal to the sum of
    the fifth power of their digits.
    """
    limit = 999999
    # It is impossible for this condition to be met > limit because 354294 < 999999
    result = 0
    for number in range(10, limit):
        if number == lpe.sum_fifth_power_of_digits(number):
            result += number
    return ''.join(('The sum of all numbers equal to the sum',
                    f' of the fifth power of their digits is {result}.'))

def pe_32():
    """Find multiplicand, multiplier and product strings that are
    pandigital e.g. 123456789.
    """
    pan_digit_products = set()
    for multiplicand in range(2, 2000):
        for multiplier in range(2, 2000):
            product = multiplicand * multiplier
            joined_string = str(multiplicand) + str(multiplier) + str(product)
            if len(str(joined_string)) == 9:
                if lpe.is_pan_digital(joined_string):
                    pan_digit_products.add(product)
    result = sum(pan_digit_products)
    return f'The sum of possible pandigital products is {result}.'

def pe_34():
    """Find all numbers that are equal to the sum of the factorial of their
    digits.
    """
    limit = 2540160
    # It is impossible for for this sum to be equal for a number > 7 * 9!
    result = 0
    for number in range(10, limit):
        if number == int(lpe.find_sum_of_digit_factorial(number)):
            result += number
    return f'The solution for Project Euler 34 is {result}'

def pe_37():
    """Find all two-sided primes i.e. primes that are truncatable both left
    and right and result in primes at each truncation.
    """
    two_sided_primes = set()
    primes = lpe.prime_sieve(1000000)
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
    return f'The sum of all two-sided primes is {result}.'

def pe_38():
    """ Find pandigital products."""
    pandigital_products = set()
    for num in range(2, 9999):
        concatenated_product = lpe.create_nine_digit_product(num)
        if lpe.is_pan_digital(concatenated_product):
            pandigital_products.add(int(concatenated_product))
    result = max(pandigital_products)
    return f'The solution for Project Euler 38 is {result}.'

def pe_41():
    """Find the largest pandigital prime possible."""
    pan_digit_primes = set()
    primes = lpe.prime_sieve(10000000)
    for prime in primes:
        if  lpe.is_pan_digital(prime):
            pan_digit_primes.add(prime)
    result = max(pan_digit_primes)
    return f'The largest possible pandigital prime is {result}.'

def pe_44():
    """Find two pentagonal numbers that have a difference and sum equal to
    another pentagonal number, specifically, the pair with the smallest
    possible difference.
    """
    pentagons_a = lpe.create_pentagon_numbers(4000)
    pentagons_b = pentagons_a.copy()
    for pent_a in pentagons_a:
        for pent_b in pentagons_b:
            difference = abs(pent_a - pent_b)
            total = pent_a + pent_b
            if difference in pentagons_a and total in pentagons_a:
                result = difference
    return f'The result for Project Euler problem 44 is {result}.'

def pe_48():
    """Find the last ten digits of the sum of the 'self powers', i.e. n ** n
    from 1 to 1000.
    """
    result = 0
    limit = 1000
    for number in range(1, limit + 1):
        result += number ** number
    result = str(result)[-10::]
    return f'The last ten digits of the sum of the self powers is {result}.'

def pe_92():
    """Find all the 'sad' numbers under 10,000,000."""
    limit = 10000000
    happy_count = 0

    for integer in range(1, limit + 1):
        if lpe.is_happy(integer):
            happy_count += 1
    sad_count = limit - happy_count
    return f'There are {sad_count} numbers from 1 to {limit} that are sad.'


pytest.main(['-v'])
