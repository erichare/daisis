import time
import numpy as np
import os

def add_test(firstNumber: float=4, secondNumber: float=5):
    # Compute the add
    print(os.environ["TEST1234"])
    time.sleep(1)
    print("Hi")
    time.sleep(1)
    result = firstNumber + secondNumber

    return result

def subtract(firstNumber: float=4, secondNumber: float=5):
    # Compute the add
    result = firstNumber - secondNumber

    return result
