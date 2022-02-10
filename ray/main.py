import ray
import time

ray.init()
print(ray.nodes())

@ray.remote
def sleep(delay):
    time.sleep(1)

def compute(delay):
    print("Beginning Ray Compute...")
    time.sleep(1)
    start = time.time()
    #print(ray.nodes())
    print("About to try")
    try:
        futures = [sleep.remote(float(delay)) for _ in range(5)]
        print("About to get...")
        ray.get(futures)
    except Exception as e:
        print("We failed")
        print(e)
        ray.shutdown()
        ray.init()
        futures = [sleep.remote(float(delay)) for _ in range(5)]
        ray.get(futures)
    print(time.time() - start)
    return str(time.time() - start)

if __name__ == "__main__":
    out = compute(1)
