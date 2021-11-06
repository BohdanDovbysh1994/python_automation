from threading import Thread

from lesson_31.rase_condition_example.employee import Employee


if __name__ == '__main__':
    employee = Employee()

    thread1 = Thread(target=employee.increase_rate)
    thread2 = Thread(target=employee.increase_rate)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(employee.rate)
