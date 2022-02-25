import numpy as np
from object_serialization.map_stack import MapStack

def compute(map_stack, map):
    status = map_stack.add_layer(map)
    return status, map_stack
