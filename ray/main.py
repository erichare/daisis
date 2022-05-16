import ray
import time
import numpy as np

ray.init(address='pebble-api-worker-748bb67786-j8p7q:6380')

def compute(val="hi"):
    return val + " bye"
