import ray
import time
import numpy as np

@ray.remote
def sleep_function(name: str = "VM1 ", duration: int = 10):
    for i in range(int(duration)):
        time.sleep(1)
        print(name, str(np.random.rand()))
    
    return 1

def compute(duration: int = 10, nb_procs: int = 4, name: str = "VM1"):
    ray.init(address='localhost:6380', ignore_reinit_error=True)

    start = time.time()
    futures = [sleep_function.remote(name = name, duration = duration) for _ in range(int(nb_procs))]
    ray.get(futures)

    return "Compute time :" + str(time.time() - start)

if __name__ == "__main__":
    out = compute()
    print(out)
