import os
import numpy as np

def compute():
    home = os.getenv("HOME")
    b = np.array([1, 1])
    np.save(home + '/b.npy', b)
    return "Success"
  
