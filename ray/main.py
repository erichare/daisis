import ray
import time
import numpy as np

ray.init(address="auto")

def compute(val="hi"):
    return val + " bye"
