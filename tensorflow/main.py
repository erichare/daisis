import tensorflow as tf
import os

print(tf.test.is_gpu_available())
print(tf.test.is_built_with_cuda())
print(os.environ)

def add_test(firstNumber: float=4, secondNumber: float=5):
    result = firstNumber + secondNumber

    print(tf.test.is_gpu_available())
    print(tf.test.is_built_with_cuda())
    print(os.environ)

    return result

def subtract(firstNumber: float=4, secondNumber: float=5):
    # Compute the add
    result = firstNumber - secondNumber

    return result
