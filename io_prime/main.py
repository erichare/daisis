# Copyright (c) 2021 Belmont Technology Inc. All rights reserved.
from math import sqrt
import time
import lorem # Test again
import os
import tempfile


def compute_bound(num_prime: int=10000):
    start = time.time()

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

    if num_prime > 100000:
        raise AssertionError("Please reduce the number to < 100,000")

    curr = 1
    numFound = 0
    generator = prime_generator()

    while numFound < int(num_prime):
        curr = next(generator)
        numFound += 1

    print("Compute Time : " + str(time.time() - start))

    return "Largest prime found: {}\n Number of primes found: {}".format(curr, numFound)


def io_bound(num_sentences: int=100000):
    start = time.time()

    if num_sentences > 1000000:
        raise AssertionError("Please reduce the num_sentences to < 1,000,000")

    sentences = [lorem.sentence() for _ in range(int(num_sentences))]

    with tempfile.TemporaryDirectory() as td:
        f_name = os.path.join(td, 'test')
        with open(f_name, 'w') as fh:
            fh.writelines(sentences)

        print("IO Time : " + str(time.time() - start))

        return "File Size: " + str(os.path.getsize(f_name))


def io_compute_bound(num_sentences: int=100000, num_prime: int=10000):
    io_result = io_bound(num_sentences)
    compute_result = compute_bound(num_prime)

    return [io_result, compute_result]
