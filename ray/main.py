import ray
import time
import numpy as np

ray.init(address='localhost:6380')

@ray.remote
def sleep_function(name = "VM1 ", duration = 10):
    for i in range(duration):
        time.sleep(1)
        print(name, str(np.random.rand()))
    
    return 1

def compute(duration = 10, nb_procs=4, name = "VM1"):
    start = time.time()
    futures = [sleep_function.remote(name = name, duration = duration) for _ in range(nb_procs)]
    ray.get(futures)

    return "Compute time :" + str(time.time() - start)

if __name__ == "__main__":
    out = compute()
    print(out)
