import ray
import time

def compute(delay):
    ray.init(local_mode=True)
    print(ray.nodes())
    
    @ray.remote
    def sleep(delay):
        time.sleep(1)

    print("Beginning Ray Compute...")
    time.sleep(1)
    start = time.time()
    #print(ray.nodes())
    print("About to try")
    futures = [sleep.remote(float(delay)) for _ in range(5)]
    print("About to get...")
    ray.get(futures)
    ray.shutdown()

    print(time.time() - start)
    return str(time.time() - start)

if __name__ == "__main__":
    out = compute(1)
