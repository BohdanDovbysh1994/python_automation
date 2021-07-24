import time


# def get_range():
#     # time.sleep(5)
#     return [1, 2, 3]
#
#
# start = time.time_ns()
# print(get_range())
# end = time.time_ns()
#
# print(f"Executed by {end - start} s")
# time.time_ns()
# time.thread_time()
# print(time.strftime("%d: %M", (1, 1, 1, 1, 1, 1, 1, 1, 1)))






# print(datetime.date(year=1991, month=12, day=20))
from datetime import datetime

today = datetime.now()


print(today.date())
print(today.time())
print(today.timestamp())
print(today.isocalendar().index(12))
