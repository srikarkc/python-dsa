import threading
import time

def worker(name, n):
    for i in range(n):
        print(f"{name}: {i}")
        time.sleep(0.1)

t = threading.Thread(target=worker, args=("A", 33))
t.start()
t.join()


from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch(url):
    # imagine an HTTP call here
    return url, len(url)

urls = ["https://a.com", "https://b.com", "https://c.com"]

with ThreadPoolExecutor(max_workers=8) as pool:
    futures = {pool.submit(fetch, u): u for u in urls}
    for fut in as_completed(futures):
        url, size = fut.result()
        print(url, size)