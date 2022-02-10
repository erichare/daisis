import ray
import time

ray.init()
print(ray.nodes())

@ray.remote
def sleep(delay):
    time.sleep(delay)

def compute(delay):
    start = time.time()
    print(ray.nodes())
    futures = [sleep.remote(float(delay)) for _ in range(15)]
    ray.get(futures)
    print(time.time() - start)
    return str(time.time() - start)

if __name__ == "__main__":
    out = compute(1)
