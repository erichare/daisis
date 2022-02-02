# Copyright (c) 2021 Belmont Technology Inc. All rights reserved.
from math import sqrt
import time


def is_prime(n: int):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True


def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n


def get_prime(number: int=9999):
    start = time.time()

    curr = 1
    numFound = 0
    generator = prime_generator()

    while numFound < int(number):
        curr = next(generator)
        numFound += 1

    print("Execution time : ", time.time() - start)

    return "Largest prime found: {}\n Number of primes found: {}".format(curr, numFound)
