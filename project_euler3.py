"""Refactoring, organization of completed Project Euler problems.
Each Project Euler problem uses a function named pe_number.
Start date: 6/21/19.
"""

import sys
import pytest
import lib_project_euler

pytest.main()

def pe_1():
    """ Return the sum of mod 5 and mod 3 integers under 1000."""
    result = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return f'Project Euler Problem 1: the sum of mod 5 and mod 3 integers under 1000 is {result}.'

def pe_2():
    """ Return the sum of all even Fibonacci numbers under 4,000,000."""
    counter = 1
    result = 0
    while lib_project_euler.fibonacci(counter) < 4000000:
        if lib_project_euler.fibonacci(counter) % 2 == 0:
            result += lib_project_euler.fibonacci(counter)
        counter += 1
    result = ('project euler Problem 2: the sum of all even Fibonacci',
              f' numbers under 4,000,000 is {result}')
    return result

def pe_3():
    """ Find the largest prime factor of the test number."""
    test_number = 600851475143
    result = max(lib_project_euler.find_prime_factors(test_number))
    return f'The largest prime factor of 600851475143 is {result}'

def pe_4():
    """PE 4. Find the largest palindromic product of two three- digit
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
    """Solve PE 5. Find the smallest number divisible by all factors
    from 1 to limit.
    """
    limit = 20
    potential_factors = lib_project_euler.prime_sieve(limit)
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
    """Solve PE 6. Find the difference between the sum of all squares of all
    numbers from 1 to 100 and the square of the sum of all numbers from 1 to
    100."""
    integers = [i for i in range(1, 101)]
    sum_of_squares = 0
    square_of_sum = (sum(integers))**2

    for i in integers:
        sum_of_squares += i**2
    answer = square_of_sum - sum_of_squares
    return f'The solution for Project Euler 6 is {answer}.'

def pe_7():
    """Solve PE 7, find the 10,001st prime number."""
    primes = list(lib_project_euler.prime_sieve(200000))
    primes.sort()
    return f'the 10,001st prime number is {primes[10000]}'

def pe_8():
    """Solve PE 8, find largest product from multiplication of 13 adjacent
    digits in file."""
    with open('files/pe_8_sample.txt') as pe_8_sample:
        sample = pe_8_sample.read()

    best_result = 0
    index = 0
    while index < len(sample) - 12:
        current_product = lib_project_euler.find_product(sample[index:index + 13])
        if current_product > best_result:
            best_result = current_product
        index += 1
    return f'{best_result} is the answer to Project Euler problem 8.'

def pe_9():
    """Solve PE 9"""
    pass

def pe_10():
    """Solve PE 10"""
    pass

def pe_11():
    """Solve PE 11"""
    pass

def pe_12():
    """Solve PE 12"""
    pass

def pe_13():
    """Solve PE 13"""
    pass

def pe_14():
    """Solve PE 14"""
    pass

def pe_15():
    """Solve PE 15"""
    pass

def pe_16():
    """Solve PE 16"""
    pass

def pe_17():
    """Solve PE 17"""
    pass

def pe_18():
    """Solve PE 18"""
    pass

def program_body():
    """Implement individual functions solving
    Project Euler problems."""
    solution_functions = {'1':pe_1(), '2':pe_2(), '3':pe_3(),
                          '4':pe_4(), '5':pe_5(), '6':pe_6(),
                          '7':pe_7(), '8':pe_8(),}
    answer = ''

    while answer != 'q':
        answer = input('What problem would you like solved? (q to quit)')
        if answer == 'q':
            return

        try:
            print(solution_functions[answer])
        except KeyError:
            print("I don't think that problem has been solved yet.")


if __name__ == "__main__":
    program_body()
    sys.exit(0)
