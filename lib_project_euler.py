"""Library of functions used by Project Euler solutions."""

def fibonacci(index, cache=None):
    """ Return the Fibbonacci number of n index. Cache results."""
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
    potential_factor = 2
    prime_factors = set()
    while potential_factor <= num:
        if num % potential_factor == 0:
            prime_factors.add(potential_factor)
            num = num/potential_factor
        else:
            potential_factor += 1
    return prime_factors

def happy_step(num):
    """Return product of one incrmental step to determine if num is happy/sad."""
    num = list(str(num))
    total = 0
    for digit in num:
        total += int(digit) ** 2
    return total

def find_product(num):
    """Find the product of a string of digits, i.e, 23 produces 6"""
    num = list(num)
    product = 1
    for digit in num:
        product = product * int(digit)
    return product

def happy_step(num):
    """Return product of one incrmental step to determine if num is happy/sad."""
    num = list(str(num))
    total = 0
    for digit in num:
        digit = int(digit)**2
        total = total + digit
    return total

