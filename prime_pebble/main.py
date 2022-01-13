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


def compute(number):
    start = time.time()

    curr = 1
    numFound = 0
    generator = prime_generator()

    while numFound < int(number):
        curr = next(generator)
        numFound += 1

    print("Execution time : ", time.time() - start)

    return [
        {
            "type": "text",
            "data": "Largest prime found: {}\n Number of primes found: {}".format(
                curr, numFound
            ),
        }
    ]


def schema():
    r = [
        {
            "id": "number",
            "type": "text",
            "label": "Number of primes to find",
            "initialValue": 9999,
            "props": {
                "type": "number"
            },
        }
    ]
    return r


if __name__ == "__main__":
    print(compute(1000))
