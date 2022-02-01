# Copyright (c) 2021 Belmont Technology Inc. All rights reserved.
from math import sqrt
import time


def is_prime(n):
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


def write_and_get_prime(number: int=9999):
    start = time.time()

    if number > 100000:
        raise AssertionError("Please reduce the number to < 100,000")

    curr = 1
    numFound = 0
    generator = prime_generator()

    while numFound < int(number):
        curr = next(generator)
        numFound += 1

    sentences = [lorem.sentence() for _ in range(number)]

    with tempfile.TemporaryDirectory() as td:
        f_name = os.path.join(td, 'test')
        with open(f_name, 'w') as fh:
            fh.writelines(sentences)

            print("Execution time : ", time.time() - start)

            return ["Largest prime found: {}\n Number of primes found: {}".format(curr, numFound),
                    "File Size: " + str(os.path.getsize(f_name))]
