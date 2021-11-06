from time import (
    time, sleep
)


def do_work():
    print("Start sleep...")
    sleep(1)
    print("End sleep...")

start = time()

for _ in range(10):
    do_work()

end = time()

print(f"Script executed in {end - start} seconds")

# Executed on I/O bound with 10.006908178329468 seconds