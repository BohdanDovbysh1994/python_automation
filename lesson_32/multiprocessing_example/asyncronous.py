from threading import Thread
from time import (
    sleep, time
)


def do_work():
    print("Start sleep...")
    sleep(1)
    print("End sleep...")

start = time()

threads = []

for _ in range(10):
    thread = Thread(target=do_work)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time()

print(f"Script executed in {end - start} seconds")