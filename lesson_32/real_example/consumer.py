from os import listdir
from time import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool


def read_report(path_to_file: str):
    with open(path_to_file) as file:
        return file.read()


PATH = "lesson_32/real_example/reports"
names = listdir(PATH)
start = time()

# synchronous approach
# Result: 43.7083158493042 seconds
# for name in names:
#     read_report(f"{PATH}/{name}")

# asynchronous approach
# Result: 15.328944444656372 seconds
# with ThreadPoolExecutor(50) as executor:
#     for name in names:
#         executor.submit(read_report, args=(f"{PATH}/{name}", ))


# parallel approach
# Result: 1.8744070529937744 seconds
# with Pool(50) as pool:
#     pool.map(read_report, (f"{PATH}/{name}" for name in names))

end = time()

print(f"Script executed in {end - start} seconds")
