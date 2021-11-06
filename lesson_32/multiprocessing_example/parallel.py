from time import sleep, time
from multiprocessing import Process


def do_work():
    print("Start sleep...")
    sleep(1)
    print("End sleep...")


start = time()

processes = []

for _ in range(10):
    process = Process(target=do_work)
    process.start()
    processes.append(process)

for process in processes:
    process.join()

end = time()

print(f"Script executed in {end - start} seconds")
