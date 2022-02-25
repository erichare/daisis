from pydaisi import Daisi
import numpy as np
from map_stack import MapStack

obj_daisi = Daisi("Object Test Eric")

nx = 200
ny = 200
ms = MapStack(nx, ny)
for i in range(10):
    ms.add_layer(np.random.rand(nx, ny))

result = obj_daisi.compute(func="compute", map_stack=ms, map=np.random.rand(nx, ny))

print(status, ms.nb_layers)

assert ms.nb_layers == 11
