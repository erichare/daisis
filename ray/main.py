import ray
import time
import numpy as np

ray.init(address='localhost:6380')

def compute(val="hi"):
    return val + " bye"
